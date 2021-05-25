#The account keeps track of the Balances
#Updated when transactions are executed 
# (if Bob sends token from Alice, then amount of tokens 
# are subtracted from Bon and added to alic's)
# in bitcoin this is the UTXO (unspend transaction inputs)
# the UTXO a trying to figure out the difference between the incomming
# and the outgoin transactions - this is a STACK ADT
# Etherium uses merkle trees and other fancy ADT to be more efficient

# This implementation is a another ADT which checks the complete history of transactions
# We implement a far more easy account model.

class AccountModel():

    def __init__(self):
        self.accounts = [] #we save the public keys of all the participants in the network at the point in time
        self.balances = {} #here we save the mapping between the public key (account) and the amount of tokens to that account
    
    def addAccount(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.accounts.append(publicKeyString)
        if publicKeyString not in self.balances:
            self.balances[publicKeyString] = 0

    def getAccount(self, publicKeyString):
        if publicKeyString in self.accounts:
            return publicKeyString
    
    def getBalance(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        return self.balances[publicKeyString]
    
    def updateBalance(self, publicKeyString, amount):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        self.balances[publicKeyString] += amount

    
