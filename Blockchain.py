from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()

    def addBlock(self, block):
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
        
    


