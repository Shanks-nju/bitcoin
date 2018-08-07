from bitcoin import *


def sign_tx(tst, private_key):
    return signall(tst, private_key)


tx = raw_input("tx: ")
key = raw_input('private key: ')

print sign_tx(tx, key)
