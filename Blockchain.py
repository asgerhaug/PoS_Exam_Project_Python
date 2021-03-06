from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake

class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()
        self.pos = ProofOfStake()

    def addBlock(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)
    
    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data
    
    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount -1:
            return True
        else:
            return False
    
    def previousBlockHashValid(self, block):
        previousBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if previousBlockchainBlockHash == block.previousHash:
            return True
        else:
            return False
    
    def getCoveredTransactionSet(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print("Transaction not covered")
        return coveredTransactions

    def transactionCovered(self, transaction):
        if transaction.type == 'EXCHANGE':
            return True
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False

    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)

    #This method executes invidual transactions within the accountModel object    
    def executeTransaction(self, transaction):
        if transaction.type == 'STAKE': 
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver: #a forger always stakes for one self, from the stakers own wallet.
                amount = transaction.amount
                self.pos.update(sender, amount)
                self.accountModel.updateBalance(sender, -amount)
        else:
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            amount = transaction.amount
            self.accountModel.updateBalance(sender, -amount)
            self.accountModel.updateBalance(receiver, amount)
    
    def nextForger(self):
        previousBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        nextForger = self.pos.forger(previousBlockHash)
        return nextForger

    def createBlock(self, transactionFromPool, forgerWallet):
        coveredTransactions = self.getCoveredTransactionSet(transactionFromPool)
        self.executeTransactions(coveredTransactions)
        previousBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        blockcount = len(self.blocks)
        newBlock = forgerWallet.createBlock(coveredTransactions, previousBlockHash, blockcount)
        self.blocks.append(newBlock) #this only appends to the node (forger)'s local version of the blockchain
        return newBlock # the returned node is yet to be broadcastet by the node

    def transactionExist(self, transaction):
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True
        return False
    
    def forverValid(self, block):
        forgerPublicKey = self.pos.forger(block.previousHash)
        proposedBlockForger = block.forger

        if forgerPublicKey == proposedBlockForger:
            return True
        else:
            return False

    # we are using a kind of "Checksum" that both transactionslists are equally long, such we assume that the Forger, did not insert a fake transaction
    def transactionsValid(self, transactions): # probably does not really guarentee any security in relation to malicius forger
        coveredTransactions = self.getCoveredTransactionSet(transactions)
        if len(coveredTransactions) == len(transactions):
            return True
        else:
            return False
    
