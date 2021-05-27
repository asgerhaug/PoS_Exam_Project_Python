from Crypto import PublicKey
from BlockchainUtils import BlockchainUtils
from TransactionPool import TransactionPool
from SocketCommunication import SocketCommunication
from Wallet import Wallet
from Blockchain import Blockchain
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils
import copy


class Node():
    def __init__(self, ip, port, key=None):
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.p2p = None
        self.ip = ip
        self.port = port
        self.blockchain = Blockchain()
        if key is not None:
            self.wallet.fromKey(key)

    
    # This methods allows us to start up the connection of the node after instantiating it, which can be handy. 
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self) #we inject a node object into SocketCommunication instances

    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    def handleTransaction(self, transaction):
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        data = transaction.payload()
        signatureValid = Wallet.signatureValid(data, signature, signerPublicKey)
        transactionExistInPool = self.transactionPool.transactionExists(transaction)
        transactionExistsInBlock = self.blockchain.transactionExist(transaction)
        if not transactionExistInPool and signatureValid and not transactionExistsInBlock:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
            forgingRequired = self.transactionPool.forgerNeed()
            if forgingRequired: 
                self.forge()
    
    def handleBlock(self, block):
        forger = block.forger
        blockHash = block.payload()
        signature = block.signature

        blockcountValid = self.blockchain.blockCountValid(block)
        previousBlockHashValid = self.blockchain.previousBlockHashValid(block)
        forgerValid = self.blockchain.forverValid(block)
        signatureValid = Wallet.signatureValid(blockHash, signature, forger)
        transactionsValid = self.blockchain.transactionsValid(block.transactions)
        
        if not blockcountValid:
            self.requestChain()

        if previousBlockHashValid and forgerValid and signatureValid and transactionsValid:
            self.blockchain.addBlock(block)
            self.transactionPool.removeFromPool(block.transactions)
        
        message = Message(self.p2p.socketConnector, 'BLOCK', block)
        encodedMessage = BlockchainUtils.encode(message)
        self.p2p.broadcast(encodedMessage)
    
    def requestChain(self):
        message = Message(self.p2p.socketConnector, 'BLOCKCHAINREQUEST', None)
        self.p2p.broadcast(BlockchainUtils.encode(message))

    def handleBlockchainRequest(self, requestingNode):
        message = Message(self.p2p.socketConnector, 'BLOCKCHAIN', self.blockchain)
        self.p2p.send(requestingNode, BlockchainUtils.encode(message))

    def handleBlockchain(self, blockchain):
        #we dont automatically overwrite the node's local version of the blockchain, but loops every block and adds the onces which are above the number of the local version.
        localBlockChainCopy = copy.deepcopy(self.blockchain)
        localBlockCount = len(localBlockChainCopy.blocks)
        receivedChainCount = len(blockchain.blocks)
        if localBlockCount < receivedChainCount:
            for blockNumber, block in enumerate(blockchain.blocks):
                if blockNumber >= localBlockCount:
                    localBlockChainCopy.addBlock(block)
                    self.transactionPool.removeFromPool(block.transactions)
            self.blockchain = localBlockChainCopy

                

    
    def forge(self):
        forger = self.blockchain.nextForger()
        if forger == self.wallet.publicKeyString():
            print('I AM THE NEXT FORGER')
            block = self.blockchain.createBlock(self.transactionPool.transactions, self.wallet)
            self.transactionPool.removeFromPool(block.transactions)
            message = Message(self.p2p.socketConnector, 'BLOCK', block)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
        else:
            print('I AM NOT THE NEXT FORGER')