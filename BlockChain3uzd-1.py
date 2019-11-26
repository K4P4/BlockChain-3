from bitcoin.rpc import RawProxy

p = RawProxy()

tx_value = 0

# Input the transaction id
tx_id = raw_input("Input the trasaction ID:")

# Retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(tx_id)

# Decode the transaction into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

# Iterate through each output in the transaction
for output in decoded_tx['vout']:
    # Add up the value of each output
    tx_value = tx_value + output['value']

tx_input = 0

# Find the sum of transaction inputs
for txinput in decoded_tx['vin']:
    raw_tx1 = p.getrawtransaction(txinput['txid'])
    decoded_tx1 = p.decoderawtransaction(raw_tx1)
    stop = txinput['vout']
    tx_input = tx_input + decoded_tx1['vout'][stop]['value']

print("Transaction fee: ", tx_input - tx_value)