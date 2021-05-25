from Crypto import Signature
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
import pprint

if __name__ == '__main__':
    
    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10,'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    previousHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount +1
    blockOne = forger.createBlock(coveredTransaction, previousHash, blockCount) 
    blockchain.addBlock(blockOne)
    pool.removeFromPool(blockOne.transactions)

    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')
    
    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    previousHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount +1
    blockTwo = forger.createBlock(coveredTransaction, previousHash, blockCount) 
    blockchain.addBlock(blockTwo)
    pool.removeFromPool(blockTwo.transactions)

    pprint.pprint(blockchain.toJson())
    #print(coveredTransaction)







