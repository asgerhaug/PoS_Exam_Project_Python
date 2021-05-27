#the selection of the forger, should be both random, but also have proportional in chance in relation to a stakers stake. 

from BlockchainUtils import BlockchainUtils
from Lot import Lot
class ProofOfStake():

    def __init__(self):
        self.stakers = {} #holds a dictionary of the peers publicKey as primary key and their stake as the mapped value.
        self.setGenesisNodeStake()
    
    #if there is no staker, then no forger, no forger, then no block, no block, then no transaction, no transactions, then no staker
    def setGenesisNodeStake(self):
        genesisPublicKey = open('keys/publicKey.pem', 'r').read()
        self.stakers[genesisPublicKey] = 10
        #self.stakers = self.update(genesisPublicKey, 1)
    
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

    #this methods validates the lots of the stakers
    def validatorLots(self, seed):#seed is the previousBlockHash
        lots = [] #lots list
        for validator in self.stakers.keys(): #we iterate over all the validators in the stakers dict
            for stake in range(self.getStake(validator)): # The stake from the validator we are currently at, we get an enumeration based on the validator's amount of stake
                lots.append(Lot(validator, stake+1, seed)) #we create a lot and define the "iteration"-parameter, based on the "stake" we are currently at, if stake E.G. = 2, its being hashchained two times
        return lots #lot instance list is returned, but who wins?
    
    def winnerLot(self, lots, seed): #seed is the previousBlockHash
        winnerLot = None #The winning-lot
        leastOffSet = None #The lot-hash with the least offset to the referenceHashIntValue - calculated as absolute distance
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16) # this is the hash, for which the staked lot-hash's will be compared
        for lot in lots: #lots get iterated and the lothash method is called which iterates the hashchaining of the number of iterations stored in the lot object
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue-referenceHashIntValue)
            if leastOffSet is None or offset < leastOffSet:
                leastOffSet = offset
                winnerLot = lot
        return winnerLot

    def forger(self, previousBlockHash): #previousBlockHash is the Seed parameter
        lots = self.validatorLots(previousBlockHash)
        winnerLot = self.winnerLot(lots, previousBlockHash)
        return winnerLot.publicKey
        

