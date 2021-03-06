import time
import copy

class Block:

  def __init__(self, transactions, previousHash, forger, blockCount):
    self.transactions = transactions
    self.previousHash = previousHash
    self.forger = forger
    self.blockCount = blockCount
    self.timestamp = time.time()
    self.signature = ''

  @staticmethod
  def genesis():
      gensisBlock = Block([],'gensisHash', 'genesis', 0)
      gensisBlock.timestamp = 0
      return gensisBlock
  
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

  def payload(self):
    jsonRepresentation = copy.deepcopy(self.toJson())
    jsonRepresentation['signature'] = ''
    return jsonRepresentation

  def sign(self, signature):
    self.signature = signature
    


