# Ethereum Gas and Estimation

Ethereum is a decentralized, open-source blockchain system that features smart contract functionality.

Smart contracts allow developers to create decentralized applications on Ethereum's blockchain.

### Units

Ethereum's native cryptocurrency is called Ether (ETH). Here are the subunits of ETH:

| Unit       | Wei Value | Ether Value  |
| ---------- | --------- | ------------ |
| Wei        | 1         | 10^(-18) ETH |
| Kwei       | 10^3      | 10^(-15) ETH |
| Mwei       | 10^6      | 10^(-12) ETH |
| Gwei       | 10^9      | 10^(-9) ETH  |
| Microether | 10^12     | 10^(-6) ETH  |
| Milliether | 10^15     | 10^(-3) ETH  |
| Ether      | 10^18     | 1 ETH        |

### Costs

The cost of transactions in Ethereum is paid in Gas, and the price of Gas is paid in Ether. Here are common terms related to costs:

- **Gas**: Measurement of computational work.
- **Gas Limit**: Maximum amount of Gas a transaction can consume.
- **Gas Price**: Amount of Ether you're willing to pay for every unit of Gas, usually measured in Gwei.
- **Transaction Fee**: Total cost of a transaction (Gas Price \* Gas Used).

### Example of Costs Calculation

Here's how you might calculate the total cost of a transaction:

| Item       | Amount      |
| ---------- | ----------- |
| Gas Price  | 50 Gwei     |
| Gas Used   | 21,000      |
| Total Cost | 0.00105 ETH |

The Total Cost is calculated as (50 _ 10^9 Wei/Gwei) _ 21,000 = 0.00105 ETH.

The Gas price can vary widely based on network congestion and other factors, so these costs can fluctuate over time.
