import hashlib
import json
from time import time
from uuid import uuid4

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
         :param block: <dict> block
         :return: <str>
        """

        #it must be ensured the dict is ordered to get right hash
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    @property
    def last_block(self):
        return self.chain[-1]      

    def proof_of_work(self, last_proof):
        """
        simple proof of work algorithm:
        - find a number p' such that hash(pp) contains leading 4 zeros, where is the previous p'
        - p is the previous proof, and p' is the new proof

        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
    
    @staticmethod
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        validates the proof: does hash contain 4 leading zeros?

        :param last_proof: <int> previous proof
        :param proof: <int> current proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    pass