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
    #ip='localhost'
    #port=10001


    node = Node(ip, port)
    node.startP2P()

    #print(coveredsTransaction)







