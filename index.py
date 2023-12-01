import hashlib

def hash_func(input):
    return '*' + input + '*'

class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash

class Blockchain:
    def __init__(self):
        genesis = Block('gen-data', 'gen-hash', 'gen-lastHash')
        self.chain = [genesis]

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash_result = hash_func(data + last_hash)
        block = Block(data, hash_result, last_hash)
        self.chain.append(block)

# Uncomment the following lines to test the blockchain

# foo_block = Block('foo-data', 'foo-hash', 'foo-lastHash')
# print(vars(foo_block))

foo_blockchain = Blockchain()

foo_blockchain.add_block('one')
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

for block in foo_blockchain.chain:
    print(vars(block))
