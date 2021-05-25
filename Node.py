from socket import IP_ADD_MEMBERSHIP
from TransactionPool import TransactionPool
from SocketCommunication import SocketCommunication
from Wallet import Wallet
from Blockchain import Blockchain

class Node():
    def __init__(self, ip, port) -> None:
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
    
    # This methods allows us to start up the connection of the node after instantiating it, which can be handy. 
    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication()



    