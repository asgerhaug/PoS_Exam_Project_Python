from BlockchainUtils import BlockchainUtils

 #the amount of token staked defines the amount of iterations
 # an account(staker) is allowed to create, and each iteration will create a lot,
 # thus increasing the stakers chance of being the next forger

class Lot():
    def __init__(self, publicKey, iteration, previousBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.previousBlockHash = previousBlockHash
    
    def lotHash(self):
        hashData = self.publicKey + self.previousBlockHash # to combine the stakers publicKey with the previous blockHash, creates non-colliding and unique hashes
        for _ in range(self.iteration): #We use a wild-card property because we dont need a value, just the amount if iterations necessary
            hashData = BlockchainUtils.hash(hashData).hexdigest() #compounding hashing, also called hash-chaining
        return hashData
    
