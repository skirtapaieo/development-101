from bitcoin import *

# Private key of Alice. You should generate your own.
alice_private_key = 'YOUR_PRIVATE_KEY'

# Get Alice's public key
alice_public_key = privtopub(alice_private_key)

# Get Alice's Bitcoin address
alice_address = pubtoaddr(alice_public_key)

# Transaction input: this is a transaction id that Alice received in the past. You should replace it.
txid = 'YOUR_TXID'

# Value of the previous transaction, you have to manually input this
previous_tx_value = 0.02

# Amount to send
amount_to_send = 0.01

# Transaction fee, you have to manually input this. This is a very simplistic approach, normally fee calculation is dynamic
transaction_fee = 0.0001

# Change to send back to Alice
change_to_send_back = previous_tx_value - amount_to_send - transaction_fee

# Output address: this is Bob's address
bob_address = 'BOB_PUBLIC_ADDRESS'

# Change address: this is Alice's change address, you should generate a new one in a real world scenario
alice_change_address = alice_address

# Create a new transaction output for Bob and for the change address
outputs = [(bob_address, amount_to_send, 'btc'), (alice_change_address, change_to_send_back, 'btc')]

# Create a new transaction input
inputs = [{'output': txid, 'value': previous_tx_value}]

# Create and sign the transaction
tx = mktx(inputs, outputs)
signed_tx = sign(tx, 0, alice_private_key)

print("Signed transaction: ", signed_tx)
