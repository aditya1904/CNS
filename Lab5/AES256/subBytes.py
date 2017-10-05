from sBox import *

def subBytes(block):
	for i in range(len(block)):
		block[i] = sbox[block[i]]
	return block

def subBytesInv(block):
	for i in range(len(block)):
		block[i] = sboxInv[block[i]]
	return block
