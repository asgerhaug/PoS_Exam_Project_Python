# class enables communctation over HTTP endpoints as a REST API
# A subcomponent within the node

from sys import meta_path
from flask_classful import FlaskView, route
from flask import Flask, jsonify, request
from werkzeug.wrappers import Response
from BlockchainUtils import BlockchainUtils


node = None

class NodeAPI(FlaskView): #NodeAPI is now a subclass of FlaskView, which now inherits its methods and attributes

    def __init__(self):
        self.app = Flask(__name__)

    def start(self, apiPort):
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host ='localhost', port=apiPort)
    
    #takes a blockchain node to inject it into NodeAPI
    def injectNode(self, injectedNode):
        global node
        node = injectedNode
    
    #what search point to access endpoint
    @route('/info', methods=['Get'])
    def info(self):
        return 'This is a communication interface to a nodes blockchain', 200 #200 means it was a successfull request
    
    @route('/blockchain', methods=['GET'])
    def blockchain(self):
        return node.blockchain.toJson(), 200

    @route('transactionPool', methods=['GET'])
    def transactionPool(self):
        transactions = {}
        for ctr, transaction in enumerate(node.transactionPool.transactions): #basically a for loop which gives a counter which can be used as an index in the dict
            transactions.update({ctr:transaction.toJson()})
            #[ctr] = transaction.toJson()
        return jsonify(transactions), 200
    
    @route('transaction', methods=['POST'])
    def transaction(self):
        values = request.get_json() #if sender sends json formatted data, otherwise "get_data" must be used
        if not 'transaction' in values:
            return 'Missing transaction value', 400
        transaction = BlockchainUtils.decode(values['transaction'])
        node.handleTransaction(transaction)
        response = {'message': 'Received transaction'}
        return jsonify(response), 201 #successfull post message code in HTTP

    