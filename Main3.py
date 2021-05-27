from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from Node import Node
import sys
import pprint

#python Main.py localhost 10001

if __name__ == '__main__':

    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyFile = None# 'keys/stakerBoBPrivateKey.pem'
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    #ip='localhost'
    #port=10003
    #apiPort=5003


    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(apiPort)

    #print(coveredsTransaction)







