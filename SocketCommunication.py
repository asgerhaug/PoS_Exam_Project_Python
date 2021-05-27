from BlockchainUtils import BlockchainUtils
from p2pnetwork.node import Node 
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
import json


class SocketCommunication(Node):
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = [] #connected nodes-list
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip, port)
    
    #this method aids the network by creating a node instance, which is always online as the first node, which peers can connect to
    def connectoToFirstNode(self):
        if self.socketConnector.port != 10001: #hardcoded port choice of first node - like a genesis node...
            self.connect_with_node('localhost',10001)# So if am not the first node (port 10001), then i connect to the 10001 socket node.

    def startSocketCommunication(self, node):
        self.node = node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectoToFirstNode()

    #when a node connects to you, you get this message"
    def inbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)
        #print('indbound connection')
        #self.send_to_node(connected_node, 'Hi I am the node you connected to')

    #when you connect to a node you get this message"
    def outbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)
        #print('outbound connection')
        #self.send_to_node(connected_node, 'Hi I am the node who initialized the connection')

    #when you get an incomming message from a node, this method is called, when transactions are issued, the node calls the handleTransactionMethod
    def node_message(self, connected_node, message):
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == 'DISCOVERY':
            self.peerDiscoveryHandler.handleMessage(message)
        elif message.messageType == 'TRANSACTION':
            transaction = message.data
            self.node.handleTransaction(transaction)
        
        

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)
