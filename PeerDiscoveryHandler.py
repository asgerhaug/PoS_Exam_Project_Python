from BlockchainUtils import BlockchainUtils
import threading
import time
from Message import Message


#This class broadcast all the nodes all the peers which is known to a specific node, which allows new nodes to connect with each other
class PeerDiscoveryHandler():

    def __init__(self, node) -> None:
        self.socketCommunication = node

    #method to start a thread
    def start(self):
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()
    
    #In order to avoid this method being executed as an endless loop, we implement threads
    def discovery(self):
        while True: #endless loop
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
            #print('discovery')
            time.sleep(10) #pauses the
    
    def status(self):
        while True:
            print('Current Connections:')
            for peer in self.socketCommunication.peers:
                print(str(peer.ip)+':'+str(peer.port))
            time.sleep(10)

    def handshake(self, connected_node):
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connected_node, handshakeMessage)

    def handshakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers #used for debugging
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodedMessage = BlockchainUtils.encode(message)
        return encodedMessage

    #"Split this into two helper methods"
    def handleMessage(self, message): #check if a peer is new and if so add it to connectionslist (socketCommunication.peers)
        peersSocketConnector = message.senderConnector 
        peersPeerlist = message.data #The list of peers which this specific messageSender knows in the network
        newPeer = True
        for peer in self.socketCommunication.peers: #Check if it is a new peer, not currently in the nodes peerlist
            if peer.equals(peersSocketConnector):
                newPeer = False
        if newPeer == True:
            self.socketCommunication.peers.append(peersSocketConnector) # adding it to the peerlist if not already present
        
        
        for peersPeer in peersPeerlist:
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown = True
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)
        
                 


