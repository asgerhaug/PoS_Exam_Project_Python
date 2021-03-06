

from Transaction import Transaction


class TransactionPool():

    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def popTransaction(self, transaction):
        self.transactions.remove(transaction)
    
    def transactionExists(self, transaction):
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
        return False

    def removeFromPool(self, transactions):
        filterPoolTransactions = []
        for poolTransaction in self.transactions:
            insert = True
            for transaction in transactions:
                if poolTransaction.equals(transaction):
                    insert = False
            if insert == True:
                filterPoolTransactions.append(poolTransaction)
        self.transactions = filterPoolTransactions
    
    #if the threshold lenght of transactionslist is reached in the pool, we initiate a forger to create the next block
    def forgerNeed(self):
        if len(self.transactions) >= 1:
            return True
        else:
            return False

            
    