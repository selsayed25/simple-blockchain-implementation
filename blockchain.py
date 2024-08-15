import hashlib
import json
from time import time

def hash_block(block):
    """
    Generate SHA-256 hash of a block.

    Args:
        block (dict): The block to be hashed.

    Returns:
        str: The SHA-256 hash of the block.
    """
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def create_block(index, previous_hash, timestamp, data, proof, hash):
    """
    Create a new block.

    Args:
        index (int): The index of the block in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The time when the block was created.
        data (list): The data contained in the block.
        proof (int): The proof of the block.
        hash (str): The hash of the block.

    Returns:
        dict: A new block.
    """
    return {
        'index': index,
        'previous_hash': previous_hash,
        'timestamp': timestamp,
        'data': data,
        'proof': proof,
        'hash': hash
    }

def proof_of_work(last_proof):
    """
    Find a proof that satisfies the proof-of-work requirement.

    Args:
        last_proof (int): The proof of the last block.

    Returns:
        int: The proof for the new block.
    """
    proof = 0
    
    while valid_proof(last_proof, proof) is False:
        proof += 1
    
    return proof

def valid_proof(last_proof, proof):
    """
    Check if the proof is valid.

    Args:
        last_proof (int): The proof of the last block.
        proof (int): The proof being tested.

    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    
    return guess_hash[:4] == "0000"

def new_block(proof, previous_hash, chain, current_data):
    """
    Create a new block and add it to the chain.

    Args:
        proof (int): The proof of the new block.
        previous_hash (str): The hash of the previous block.
        chain (list): The blockchain.
        current_data (list): The data to be added to the new block.

    Returns:
        dict: The newly created block.
    """
    block = create_block(
        index = len(chain) + 1,
        previous_hash = previous_hash or hash_block(chain[-1]),
        timestamp = time(),
        data = current_data,
        proof = proof,
        
        hash = hash_block(create_block(
            index = len(chain) + 1,
            previous_hash = previous_hash or hash_block(chain[-1]),
            timestamp = time(),
            data = current_data,
            proof = proof,
            hash = ""
        ))
    )
    
    current_data.clear()
    chain.append(block)
    return block

def new_data(current_data, data):
    """
    Add new data to the list of current transactions.

    Args:
        current_data (list): The list of current data in the blockchain.
        data (str): The data to be added.

    Returns:
        int: The index of the block that will hold this data.
    """
    return len(current_data.append(data)) + 1

def last_block(chain):
    """
    Get the last block in the chain.

    Args:
        chain (list): The blockchain.

    Returns:
        dict: The last block in the chain.
    """
    return chain[-1]

if __name__ == "__main__":
    chain = []
    current_data = []
    
    # Create the genesis block
    new_block(proof=100, previous_hash='1', chain=chain, current_data=current_data)
    
    print("Welcome to the Blockchain!")
    
    while True:
        command = input("Enter command (new_data, new_block, quit): ")
    
        if command == 'new_data':
            data = input("Enter data: ")
            new_data(current_data, data)
            print("Data added!")
    
        elif command == 'new_block':
            last_block_data = last_block(chain)
            last_proof = last_block_data['proof']
            proof = proof_of_work(last_proof)
            new_block(proof, previous_hash=None, chain=chain, current_data=current_data)
            print("Block added!")
    
        elif command == 'quit':
            break
    
        else:
            print("Unknown command")
