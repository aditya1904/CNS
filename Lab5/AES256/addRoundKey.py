def addroundkey(block,roundKey):
	for i in range(len(block)):
		block[i] = block[i] ^ roundKey[i]
	return block
