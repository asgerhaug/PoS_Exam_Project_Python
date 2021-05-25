from p2pnetwork.node import Node 


class SocketCommunication(Node):
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)

    def startSocketCommunication(self):
        self.start()

    #when a node connects to you, you get this message"
    def inbound_node_connected(self, connected_node):
        print('indbound connection')
        self.send_to_node(connected_node, 'Hi I am the node you connected to')

    #when you connect to a node you get this message"
    def outbound_node_connected(self, connected_node):
        print('outbound connection')
        self.send_to_node(connected_node, 'Hi I am the node who initialized the connection')

    #when you get an incomming message from a node, this method is called
    def node_message(self, connected_node, message):
        print(message)
