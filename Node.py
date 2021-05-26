from BlockchainUtils import BlockchainUtils
from TransactionPool import TransactionPool
from SocketCommunication import SocketCommunication
from Wallet import Wallet
from Blockchain import Blockchain
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils


class Node():
    def __init__(self, ip, port):
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.p2p = None
        self.ip = ip
        self.port = port
        self.blockchain = Blockchain()
    
    # This methods allows us to start up the connection of the node after instantiating it, which can be handy. 
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    def handleTransaction(self, transaction):
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        data = transaction.payload()
        signatureValid = Wallet.siganatureValid(data, signature, signerPublicKey)
        transactionExist = self.transactionPool.transactionExists(transaction)
        if not transactionExist:
            self.transactionPool.addTransaction(transaction)




#        if not transactionExists and signatureValid:
 #           self.transactionPool.addTransaction(transaction)
  #          message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
   #         encodedMessage = BlockchainUtils.encode(message)
    #        self.p2p.broadcast(encodedMessage)
    