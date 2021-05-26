

class ProofOfStake():

    def __init__(self):
        self.stakers = {} #holds a dictionary of the peers publicKey as primary key and their stake as the mapped value.
    
    
    def update(self, publicKeyString, stake):
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake
    
    def getStake(self, publicKeyString):
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None