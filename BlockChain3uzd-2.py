from bitcoin.rpc import RawProxy
import sys
import getopt
import hashlib

# Function for converting from big-endian to littl-endian (switch most significant with least significant byte at the front)
def endianConversion(input1):
    ba = bytearray.fromhex(input1)
    ba.reverse()
    result = ''.join(format(x, '02x') for x in ba)
    return result

p = RawProxy()

# Write down basic block informaction
blockHeight = int(sys.argv[1])

blockHash = p.getblockhash(blockHeight)

blockHeader = p.getblock(blockHash)


# Gets the full header information in hex format
fullHeader = (endianConversion(blockHeader['versionHex']) + endianConversion(blockHeader['previousblockhash']) 
+ endianConversion(blockHeader['merkleroot']) + endianConversion('{:02x}'.format(blockHeader['time']))
+ endianConversion(blockHeader['bits']) +  endianConversion('{:02x}'.format(blockHeader['nonce'])))

binHeader = fullHeader.decode('hex')

# Calculates the hash based on the header information
calculatedHash = hashlib.sha256(hashlib.sha256(binHeader).digest()).digest()

if calculatedHash[::-1].encode('hex_codec')==blockHeader['hash']:
    print("Block hash is correct")
else:
    print("Block hash is incorrect")