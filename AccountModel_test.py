from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

wallet = Wallet()
publicKeyString = wallet.publicKeyString()
accountModel = AccountModel()

def test_getBalance() -> None:
    accountModel.addAccount(publicKeyString)
    assert accountModel.getBalance(publicKeyString) == 0

def test_updateBalance() -> None:
    accountModel.updateBalance(publicKeyString,5)
    assert accountModel.getBalance(publicKeyString) == 5

