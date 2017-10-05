from keyManager import *
from addRoundKey import *
from rowShifter import *
from columnMixer import *

def encrypt(block,key):
	expandedKey = expandKey(key)
	roundKey = createRoundKey(expandedKey,0)
	block = addroundkey(block,roundKey)

	for i in range(1,14):
		roundKey = createRoundKey(expandedKey,i)
		block = subBytes(block)
		block = shiftRow(block)
		block = mixColumns(block)
		block = addroundkey(block,roundKey)

	roundKey = createRoundKey(expandedKey,14)
	block = subBytes(block)
	block = shiftRow(block)
	block = addroundkey(block,roundKey)
	return block

def decrypt(block,key):
	expandedKey = expandKey(key)
	roundKey = createRoundKey(expandedKey,14)
	block = addroundkey(block,roundKey)
	block = shiftRowInv(block)
	block = subBytesInv(block)

	for i in range(13,0,-1):
		roundKey = createRoundKey(expandedKey,i)
		block = addroundkey(block,roundKey)
		block = mixColumnsInv(block)
		block = shiftRowInv(block)
		block = subBytesInv(block)

	roundKey = createRoundKey(expandedKey,0)
	block = addroundkey(block,roundKey)
	return block
