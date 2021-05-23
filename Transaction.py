# Background information
# Transactions are the basic building blocks of any DLT
# They are essential for the change of the Blockchains state
# Properties depend on the type of transaction, but a basic set includes:
# -   Signatures, sender, receiver, timestamp and data are examples of properties

# Types of transactions:
# Transfer Transaction between Alice and Bob
# Exchange Transactions is changing fiat currency for crypto and vice versa for E.G. alice
# Stake Transactions - Alice or Bob sends tokens to the Stake, in order to increase chances of being the forger (creator of the new block)

# library import for creating unique id's with guarenteed non-collisions. 
import uuid
import copy

# library import for 
import time

class Transaction:
    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = '' 
    
    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature
    
    #generates a deep copy of the original object, but sets the signature string to '', such taht we can validate it eve after signing it 
    def playload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False

    
