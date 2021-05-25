from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
import pprint

wallet = Wallet()
pool = TransactionPool()

blockchain = Blockchain()
previousHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
blockCount = blockchain.blocks[-1].blockCount + 1

alice = Wallet()
bob = Wallet()
exchange = Wallet()

def test_exchange_transfer_sameblock() -> None:
    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10,'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    assert blockchain.transactionCovered(pool.transactions[0]) == True
    assert blockchain.transactionCovered(pool.transactions[1]) == False 


def test_transactions_covered() -> None:
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')
    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)
    assert blockchain.transactionCovered(pool.transactions[0]) == False 

def test_previous_BlockHash_isValid() -> None:
    block = wallet.createBlock(pool.transactions,previousHash, blockCount)
    assert blockchain.previousBlockHashValid(block) == True

def test_previous_BlockHash_is_not_valid() -> None:
    block = wallet.createBlock(pool.transactions,'fakeHash', blockCount)
    assert blockchain.previousBlockHashValid(block) == False

def test_blockCount_is_valid() -> None:
    block = wallet.createBlock(pool.transactions,previousHash, blockCount)
    assert blockchain.blockCountValid(block) == True

def test_blockCount_is_not_valid() -> None:
    fakeCount = blockCount +2
    block = wallet.createBlock(pool.transactions,previousHash, fakeCount)
    assert blockchain.blockCountValid(block) == False
