from bitcoin import *

my_private_key = random_key()
print(my_private_key)
my_public_key = privtopub(my_private_key)
print(my_public_key)
my_bitcoin_address = pubtoaddr(my_public_key)
print(my_bitcoin_address)
