from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests
from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random

# a random strin generator

def getRandomString(lenght):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(lenght))
    return resultString #uses as the seed.

# we do a test to see if they have an equal porportional chance of wining the forger.
if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('bob', 40) 
    pos.update('alice', 60)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == 'bob':
            bobWins += 1
        elif forger == 'alice':
            aliceWins += 1

    print('bob won: ' + str(bobWins) +' times')
    print('Alice won: ' + str(aliceWins)+ ' times')
    print('win-lose coefficient bob/alice: '+ str(bobWins/aliceWins))

