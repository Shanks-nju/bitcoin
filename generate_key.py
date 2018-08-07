import bitcoin

private_key = bitcoin.random_key()
compressed_private_key = private_key + '01'

print("Private Key is:", private_key)
print("Private Key Appending 01 is:", compressed_private_key)

public_key = bitcoin.privkey_to_pubkey(compressed_private_key)
print("Public key is:", public_key)

print("Compressed BitCoin Address (b58Check) is:", bitcoin.pubkey_to_address(public_key))
