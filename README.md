# Simple Blockchain Implementation

This project implements a simple blockchain to understand the fundamentals of how blockchains function. The blockchain includes basic features such as adding data to the chain, mining new blocks, and ensuring the chain's integrity through proof of work. This is part of my series on weekly "Codects" (coding + projects), where I aim to code and learn more about tech through research and development.

## Features

Here are the features of the simple blockchain application:

- **Block Creation**: Create new blocks with data, timestamp, and hash.
- **Proof of Work**: Simple proof-of-work algorithm to mine new blocks.
- **Chain Management**: Add blocks to the chain and validate them.
- **Command-Line Interface**: Interact with the blockchain through a terminal-based interface.

## How does this work?

1. **Block Structure**: Each block contains an index, previous hash, timestamp, data, and its own hash.
2. **Hashing**: Uses SHA-256 hashing to secure block data.
3. **Proof of Work**: Ensures new blocks meet a difficulty requirement (hash starting with '0000').
4. **Chain Management**: Adds new blocks to the blockchain and maintains a list of current transactions.

## Installation

1. **Clone the respository**:

```
git clone https://github.com/selsayed25/simple-blockchain-implementation.git
cd simple-blockchain-implementation
```

2. **Ensure Python is installed**: This project uses Python 3. Make sure that you have Python 3 (any version of it *should* work) installed on your system.

## Usage

1. **Run the script**: Navigate to the project directory, where the `blockchain.py` file is saved, and run:

```
python ./blockchain.py
```

2. **Interact with the Blockchain**:

- **Add Data**: Enter `new_data` and provide the data to add to the blockchain.
- **Mine a Block**: Enter `new_block` to mine a new block and add it to the chain.
- **Quit**: Enter `quit` to exit the application.
