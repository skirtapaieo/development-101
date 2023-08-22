// Ethers installed

// Create account at Infura.io

// Select Web3 API

// Copy API key

//

import { ethers } from 'ethers';

const = API_KEY = "kjasedflkjsadflkajsd"

const network = "homestead"

const provider = ethers.providers.InfuraProvider(network, API_KEY)

const blockNumber = await provider.getBlockNumber()
console.log(blockNumber);

// Metamask

