from inspect import BoundArguments
from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests

def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), amount, type)

    url = 'http://localhost:5000/transaction'
    package = {'transaction': BlockchainUtils.encode(transaction)} #data created
    request = requests.post(url, json=package)
    #print(request.text)



if __name__ == '__main__':

    #lot = Lot('bob', 1, 'lastHash')
    #print(lot.lotHash())

    bob = Wallet()
    #bob.fromKey('keys\stakerBobPrivateKey.pem')
    alice = Wallet()
    alice.fromKey('keys\stakerAlicePrivateKey.pem')
    exchange = Wallet()

    #forger: genesis
    postTransaction(exchange, alice, 101, 'EXCHANGE')
    postTransaction(exchange, bob, 99, 'EXCHANGE')
    postTransaction(alice, alice, 50, 'STAKE')

    #forger likely alice
    #postTransaction(alice, alice, 50, 'STAKE')
    postTransaction(bob, alice, 1, 'TRANSFER')
    #postTransaction(alice, bob, 1, 'TRANSFER')

    #forger likely bob
    #postTransaction(alice, bob, 1, 'TRANSFER')
    #postTransaction(alice, bob, 1, 'TRANSFER')
    #postTransaction(bob, bob, 100, 'STAKE')
    #postTransaction(bob, alice, 1, 'STAKE')


    #transaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')

