class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self):
        #will add a new block to the blockchain
        pass
    
    def new_transaction(self):
        #adds new transaction to transactions list
        pass

    @staticmethod
    def hash(block):
        #will hash a block
        pass

    @property
    def last_block(self):
        #return last block in chain
        pass        

    pass