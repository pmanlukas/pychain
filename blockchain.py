import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #Create a genisis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (optional) <str> Hash of previous block
        :return: <dict> new Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        #reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the receipient
        :param amount: <int> Amount
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        creates a sha-256 hash of a block 
         :param
        """
    @property
    def last_block(self):
        return self.chain[-1]      

    pass