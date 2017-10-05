def getKey(filename):
	len_key = 64
	keyfile = open(filename, 'r')
	hexadecimalkey = keyfile.read()
	keyarray = []
	for i in range(0, len_key, 2):
		keyarray.append(int(hexadecimalkey[i:i+2], 16))
	return keyarray
