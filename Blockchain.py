import hashlib


class BlueCoin:
    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        self.blockData = " - " .join(transaction_list) + " - " + prev_block_hash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()


t1 = "Tom sends 5 BC to Dan"
t2 = "Dan sends 2 BC to Anna"
t3 = "Anna sends 3.5 BC to Bruce"
t4 = "Bruce sends 0.3 BC to Mary"
t5 = "Mary sends 1.5 BC to Tom"
t6 = "Anna send 3 BC to Dan"

initial_block = BlueCoin("Initial String", [t1, t2])

print(initial_block.blockData)
print(initial_block.blockHash)

second_block = BlueCoin(initial_block.blockHash, [t3, t4])
print(second_block.blockData)
print(second_block.blockHash)

third_block = BlueCoin(second_block.blockHash, [t5, t6])
print(third_block.blockData)
print(third_block.blockHash)

# N.B - You cannot disrupt the integrity of the blockchain in a previous transaction because the blockchain is
# based on previous transactions from the hash.

