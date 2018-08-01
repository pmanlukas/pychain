class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self):
        #will add a new block to the blockchain
        pass
    
    def new_transaction(self, sender, recipient, amount):
        #adds new transaction to transactions list
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
        #will hash a block
        pass

    @property
    def last_block(self):
        #return last block in chain
        pass        

    pass