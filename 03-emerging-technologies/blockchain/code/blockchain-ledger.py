import hashlib
import time

# Transaction class representing a single transaction
class Transaction:
    def __init__(self, from_person, to_person, amount):
        self.from_person = from_person
        self.to_person = to_person
        self.amount = amount

# Block class representing a block in the blockchain
class Block:
    def __init__(self, previous_hash, transaction):
        self.timestamp = time.time()  # Time of block creation
        self.transaction = transaction  # Transaction details
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.hash = self.get_hash()  # Hash of the current block

    # Method to calculate the hash of the block
    def get_hash(self):
        # We combine all the data of the block to generate the hash
        header_bin = (str(self.previous_hash) +
                      str(self.transaction.from_person) +
                      str(self.transaction.to_person) +
                      str(self.transaction.amount) +
                      str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

# Blockchain class representing the blockchain
class Blockchain:
    def __init__(self):
        self.blocks = [self.get_genesis_block()]  # Initialize blockchain with genesis block

    # Method to create a genesis block
    def get_genesis_block(self):
        return Block("0", Transaction("Genesis", "Genesis", 0))

    # Method to add a new block to the blockchain
    def add_block(self, from_person, to_person, amount):
        transaction = Transaction(from_person, to_person, amount)
        new_block = Block(self.blocks[-1].hash, transaction)  # Create a new block
        self.blocks.append(new_block)  # Add the new block to the chain

    # Method to get the entire blockchain data
    def get_chain(self):
        chain_data = []
        for block in self.blocks:
            chain_data.append({
                'Timestamp': block.timestamp,
                'Transaction': {
                    'From': block.transaction.from_person,
                    'To': block.transaction.to_person,
                    'Amount': block.transaction.amount
                },
                'Hash': block.hash
            })
        return chain_data

