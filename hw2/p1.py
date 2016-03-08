from binascii import unhexlify, hexlify
##Add a and b in GF(2^8)
def add(a, b):
	return hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(a[-len(b):]), unhexlify(b))))

#generate tables/do other stuff

##Multiply a and b in GF(2^8)
#def multiply(a, b):
	#

test1 = '00'
test2 = '00'
print add(test1, test2)
