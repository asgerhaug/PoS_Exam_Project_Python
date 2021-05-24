from Crypto import Signature
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction

#The wallet class uses RSA key-pair generation to generate a unique set private-public key for the wallet object

class Wallet():
    
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    #Signature creation
    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        SignatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        Signature = SignatureSchemeObject.sign(dataHash)
        return Signature.hex()

    #it makes sense to validate signatures without needing to create an object
    @staticmethod
    def siganatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        SignatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = SignatureSchemeObject.verify(dataHash, signature)
        return signatureValid

    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

    def createTransaction(self, receiver, amount, type):
        transaction = Transaction(self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.playload())
        transaction.sign(signature)
        return transaction

