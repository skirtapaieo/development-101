# blockchain-dapp-mining-101

- [Building a Web3 dApp - a decentralized art marketplace](#building-a-web3-dapp---a-decentralized-art-marketplace)
- [BlockchainExpert Course](#blockchainexpert-course)
- [Mining](#mining)
- [Creating a Wallet]("creating-a-wallet)
- [Setting up a Node]("setting-up-a-node)
  
<br>

# Part 1 - Building a Web3 dApp - a decentralized art marketplace 

<br> 

We are creating a decentralized marketplace, for digital art. 

## Smart contract 

Central to the dApp will be a "smart contract", that will be deployed on Ethereum. 

Example of a Smart Contract, written in Solidity: https://github.com/skirtapaieo/blockchain-101/blob/main/code/smart-contract.sol

```
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ArtMarketplace is ERC721 {
    uint public artId = 0;

    constructor() ERC721("ArtMarketplace", "ART") public {}

    function mintArt(string memory _tokenURI) public {
        _mint(msg.sender, artId);
        _setTokenURI(artId, _tokenURI);
        artId++;
    }
    
    function buyArt(uint _artId) public payable {
        require(msg.value >= 0.01 ether, "Not enough ETH sent; check price!");
        _transfer(ownerOf(_artId), msg.sender, _artId);
    }
}
```

This contract (is simplified) and creates a new ERC721 token (the standard for NFTs on Ethereum) each time an artist minds new art. The string points to a JSON object stored off-chain on IPFS - Internet Planetary File System. The buy function assumes a fixed price. 


## Front-end 

- The front-end could be a simple application written in JavaScript. 
- The front-end could use Web3.js or Ethers.js to interact with the Etherreum blockchain. 
- Users could browse listed art
- when decides to buy would initiat a transaction to call the "buyArt" function in the smart contract
- users need to confirm this transactions in their Ethereum wallet (like Metamask)
- artists need an interfact to upload their art, provide details and mint their NFT's by calling the mintArt function (in the smart contract) 

### Setup and connect to MetaMask (Ethereum wallet provider enables interactions with decentralized applications) 

```
const Web3 = require('web3');
let web3;

if (window.ethereum) {
    web3 = new Web3(window.ethereum);
    window.ethereum.enable();
} else if (window.web3) {
    web3 = new Web3(window.web3.currentProvider);
} else {
    console.log('Non-Ethereum browser detected. Consider trying MetaMask!');
}
```

We check if MetaMask is installed, then MetaMask (or other) is installed in the users browser, the Web3 instance is then created, and enable is used to get the user's permission to access their Ethereum account. Then it checks for the older way and if neither exists/works it means that the user does not havea web3 provider and therefore cannot interact with the Ethereum blockchain. 

### Get the deployed contract 

```
const contractAddress = "<your_contract_address_here>";
const ABI = <your_contract_ABI_here>; // This is the contract's ABI

// get the contract instance
const contract = new web3.eth.Contract(ABI, contractAddress);

```


## Buy art 

```
const contract = new web3.eth.Contract(contractABI, contractAddress);
```

**web3.eth.Contract** is a function in web3.js that creates a new contract instance with all its methods and events defined in its JSON interface object, which is ABI (Application Binary Interface) in this case.

**contractABI** is the ABI of your contract. The ABI is a JSON array that defines how to interact with the contract: it specifies the contract's functions, their names, return types, and other information. You get the ABI when you compile your Solidity contract.

**contractAddress** is the address where your contract is deployed on the Ethereum network.

The resulting **contract** object allows us to interact with the contract from your JavaScript code 

## Mint Art (from Smart Contract)

```
async function mintArt(name, description, price) {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    await contract.methods.mintArt(name, description, price)
        .send({from: account})
        .on('transactionHash', function(hash){
            // This callback gets triggered when the transaction is being mined.
            console.log('transactionHash', hash);
        });
}
```



## Decentralized storage

## Identity 

## DAO 


<br>

# Part 2 - BlockchainExpert Course

- [Web 1.0, 2.0, 3.0](#web-10-20-30)
- [Centralized vs Decentralized](#centralized-vs-decentralized)
  - [Centralized (controlled by a single entity)](#centralized-controlled-by-a-single-entity)
  - [Decentralized](#decentralized)
- [Ledgers](#ledgers)
- [Wallets](#wallets)
- [Transactions](#transactions)
- [Blocks](#blocks)
- [Blockchain security](#blockchain-security)
  
<br>

## Introduction and Blockchain Fundamentals 

### web 1.0, 2.0, 3.0 

- Web 1.0 - read-only internet, no advertising 
- Web 2.0 - current state of web, centralized ownership, heavy advertising, front-end focus  
- Web 3.0 - idea around the future, decentralized control, more back-end focus

### centralized vs decentralized 

#### Centralized (controlled by a single entity) 
- google 
- coinbase
- banks 
- amazon 
- US government 
- whats app 

#### Decentralized
- Bitcoin 
- Ethereum 
- DeFi
- DAO's 
- IPFS
- Tor Network
- Decentralized Social Media (BlueSky)
- Open Source SW projects (often decentralized)

### Ledgers 

https://github.com/skirtapaieo/blockchain-101/blob/main/code/blockchain-ledger.py


### Wallets 

https://github.com/skirtapaieo/blockchain-101/blob/main/code/bitcoin-keys-and-address.py
https://github.com/skirtapaieo/blockchain-101/blob/main/code/encrypt-decrypt.py
https://github.com/skirtapaieo/blockchain-101/blob/main/code/wallet-example.py

### Transactions 

https://github.com/skirtapaieo/blockchain-101/blob/main/code/create-transaction.py

### Blocks 

Maz supply of Bitcoin is 21 M BTC, currently 19.1 is used. Satoshi Nakamoto inventor (pseudonym). A block is approximately 1 MB, and it is enough to store approx 2000 transactions. 
https://github.com/skirtapaieo/blockchain-101/blob/main/models/block.model.png

### Blockchain security 

- Decentralization makes it harder to compromise the network
- Cryptography used to secure data, digital signing using private key, all data is hashed
- 51% attack is when an entity controls more than 50% of Bitcoin mining hash rate (the processing power)

## Ethereum and Smart Contracts 

## Solidity Fundamentals 

## Advanced Solidity 

## Interacting with Smart contracts

## Web3 tools 

## Projects 


<br>

# Part 3 - Mining 

Mining is a process of creating new blocks on the Bitcoin blockchain

**Requisites for mining** 

```
# Obtain necessary hardware
asic_miner = acquire_ASIC_miner()

# Install and set up Bitcoin client software
bitcoin_client = install_bitcoin_client()

# Synchronize the blockchain
blockchain = bitcoin_client.synchronize_blockchain()

# Ensure constant internet connection
internet_connection = ensure_internet_connection()

```


**Transaction Verification**
Miners pickup several unconfirmed transactions from the Bitcoin network's mempool.

```
# Fetch transactions from mempool
mempool_transactions = rpc_connection.getrawmempool()

# For each transaction in mempool
for txid in mempool_transactions:
    # Get the transaction details
    raw_tx = rpc_connection.getrawtransaction(txid)
    tx_details = rpc_connection.decoderawtransaction(raw_tx)
    
    # Verify the transaction
    # Note: In reality, Bitcoin nodes do this automatically
    if verify_transaction(tx_details):
        valid_transactions.append(tx_details)
```

**Block Creation** 
They then compile these transactions into a 'block'. 
```
# Create a new block with the valid transactions
new_block = create_new_block(valid_transactions)

```

**Proof-of-Work**
The miners' computers then try to find a nonce (a random number) that, when hashed with the rest of the content of the block, produces a hash with a certain number of leading zeroes (according to the current difficulty target). This step involves repeatedly changing the nonce and hashing the block until a suitable hash is found. This is the 'work' in Proof-of-Work.

```
# Try to solve the proof of work for the block
while not is_valid_proof(new_block):
    # Change the nonce
    new_block['nonce'] += 1
```

**Adding Block to the Chain** 
Once a miner finds a nonce that results in a suitable hash, they broadcast this block to the rest of the network. 
If two miners solve the proof-of-work problem at roughly the same time, the network will temporarily "fork" into two separate chains. 
However, the tie is broken as soon as a miner mines another block on top of one of these blocks. 
The longest chain always wins, and any blocks not in the longest chain are discarded. Any transactions in those blocks that aren't in the winning blocks are returned to the mempool to be included in future blocks.
```
# Submit the new block to the network
submit_block(new_block)

# If another block is broadcast at the same time and causes a fork
if blockchain_forked():
    # Follow the longest chain
    follow_longest_chain()
```
**Reward** 
The miner who found the suitable hash is rewarded with newly minted Bitcoin (the block reward) and transaction fees from the transactions included in the block.
```
# The miner's reward is automatically added to their address in the blockchain
```

<br>

# Creating a Wallet 

It is very simple, using Metamask for example. Then if you're from Sweden you need Coinbase or Binance, to deposit funds to actually buy Eth. 
<br>

# Setting up a Node

Running an Ethereum node means running software (an Ethereum client) that connects to the Ethereum network and maintains a copy of the entire blockchain on your device. The node verifies all transactions and blocks (following the Ethereum protocol rules) and can be used to submit new transactions to the network.

There are several types of nodes you can run:

- Full Node: This type of node downloads the entire blockchain to your device and fully verifies all transactions and blocks. It can be used to mine new blocks (if it's also a mining node).

- Light Node (or Light Client): A light node only downloads a small portion of the blockchain, relying on full nodes for additional information. It's useful for devices with less storage capacity.

- Archive Node: This node maintains the entire blockchain history along with all historical states and can be used to query any state at any point in time.

Running an Ethereum node contributes to the decentralization and security of the network. It allows you to interact with the Ethereum network without relying on a third party, ensuring you can verify transactions yourself.

There are several Ethereum clients that you can use to run a node, including but not limited to:

- Geth: The most popular Ethereum node software, written in Go.
- Parity: An Ethereum client written in Rust, known for its speed.
- Nethermind: An Ethereum client written in .NET Core.

The process of running a node involves downloading the client software, syncing it with the Ethereum network (which can take several hours to days, depending on the type of node), and then keeping it online to stay synced with new blocks.

