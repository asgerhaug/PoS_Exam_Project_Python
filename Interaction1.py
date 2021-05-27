from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests
from ProofOfStake import ProofOfStake
from Lot import Lot


if __name__ == '__main__':

    #lot = Lot('bob', 1, 'lastHash')
    #print(lot.lotHash())

    bob =  Wallet()
    alice = Wallet()
    exchange = Wallet()

    transaction = exchange.createTransaction(alice.publicKeyString(), 100, 'EXCHANGE')

    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)} #data created
    request = requests.post(url, json=package)
    print(request.text)

