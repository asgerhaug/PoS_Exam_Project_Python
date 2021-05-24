import datetime

class Block:

  def __init__(self, transactions, previousHash, forger, blockCount):
    self.transactions = transactions
    self.previousHash = previousHash
    self.forger = forger
    self.blockCount = blockCount
    self.timestamp = datetime.datetime.now()
    self.signature = ''

  def toJson(self):
    data = {}
    data['previousHash'] = self.previousHash
    data['forger'] = self.forger
    data['blockCount'] = self.blockCount
    data['timestamp'] = self.timestamp
    data['signature'] = self.signature
    jsonTransactions = []
    for transaction in self.transactions:
        jsonTransactions.append(transaction.toJson())
    data['transactions'] = jsonTransactions
    return data


