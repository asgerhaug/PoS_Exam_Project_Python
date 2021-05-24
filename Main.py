from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    
    
wallet = Wallet()
fakewallet = Wallet()
pool = TransactionPool()


transaction = wallet.createTransaction(receiver, amount, type)
#print(transaction.playload())

#signatureValid = Wallet.siganatureValid(
#    transaction.playload(), transaction.signature, wallet.publicKeyString())
 #   transaction.playload(), transaction.signature, fakewallet.publicKeyString())##

# print(signatureValid)

if pool.transactionExists(transaction) == False:
    pool.addTransaction(transaction)

block = Block(pool.transactions, 'previousHash', 'forger', 1)

print(block.toJson())

