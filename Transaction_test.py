from Transaction import Transaction
from Wallet import Wallet

def test_transaction_signature_true() -> None:
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    
    transaction = Transaction(sender, receiver, amount, type)
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    transaction.sign(signature)
    signatureValid = wallet.siganatureValid(transaction.playload(), signature, wallet.publicKeyString())
    assert signatureValid == True

def test_transaction_signature_false() -> None:
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    
    transaction = Transaction(sender, receiver, amount, type)
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    transaction.sign(signature)
    signatureValid = wallet.siganatureValid(transaction.toJson(), signature, wallet.publicKeyString())
    assert signatureValid == False