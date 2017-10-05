from subBytes import *

def keyScheduleCore(word, i):
	newWord = word[1:]+word[:1]
	subBytes(newWord)
	newWord[0] = newWord[0] ^ rCon[i]
	return newWord

def expandKey(cipherKey):
	cipherKeySize = len(cipherKey)
	assert cipherKeySize == 32
	expandedKey = []
	currentSize,rconIter = 0,1

	t = [0,0,0,0]

	for i in range(cipherKeySize):
		expandedKey.append(cipherKey[i])
	currentSize += cipherKeySize

	while currentSize < 240:
		for i in range(4):
			t[i] = expandedKey[(currentSize - 4) + i]
		if currentSize % cipherKeySize == 0:
			t = keyScheduleCore(t, rconIter)
			rconIter += 1
		if currentSize % cipherKeySize == 16:
			for i in range(4):
				t[i] = sbox[t[i]]
		for i in range(4):
			expandedKey.append(((expandedKey[currentSize - cipherKeySize]) ^ (t[i])))
			currentSize += 1
	return expandedKey

def createRoundKey(expandedKey,i):
	return expandedKey[i*16:i*16+16]
