from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    
    
    # transaction = Transaction(sender, receiver, amount, type)

    # wallet = Wallet()
   # signature = wallet.sign(transaction.toJson())

  #  transaction.sign(signature)
 #   print(transaction.toJson())
#
 #   signatureValid = wallet.siganatureValid(transaction.playload(), signature, wallet.publicKeyString())
#    print (signatureValid)

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

if pool.transactionExists(transaction) == False:
    pool.addTransaction(transaction)

print(pool.transactions)