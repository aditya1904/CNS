import readKeyFile
from readBlockFile import *
from AES256 import *
import argparse
from argparse import RawTextHelpFormatter
import time

parser = argparse.ArgumentParser(description='AES 256-bit encrypt and decrypt', formatter_class=RawTextHelpFormatter)
parser.add_argument('mode',help="encrypt or decrypt")
args = parser.parse_args()

mode = str(args.mode).lower()

def fileEncrypt():
	start = time.clock()
	block = getEncryptBlock("testBlock")
	print len(block)
	startkrypt = time.clock()
	key = readKeyFile.getKey("testKey")
	outfile = open("encrypted_file","wb")
	strangen = ""
	cryptLargeblock = []
	for i in range(len(block)):
		cryptLargeblock.append(encrypt(block[i],key))

	while i < len(cryptLargeblock):
		for row in cryptLargeblock:
			for item in row:
				strangen += hex(item)[2:].zfill(2)
		i += 1
	outfile.write(strangen)
	outfile.close()
	kryptelapsed = time.clock()-startkrypt
	elapsed = time.clock()-start
	print len(cryptLargeblock)
	print "Total Tid: " + str(elapsed)
	print "Krypteringstid: " + str(kryptelapsed)

def fileDecrypt():
	start = time.clock()
	key = readKeyFile.getKey("testKey")
	file = open("decrypted_file","wb")
	decrypttime = time.clock()
	decryptBlock = []
	decString = ""
	eblock = getDecryptBlock("encrypted_file")
	print len(eblock)

	for i in range(len(eblock)):
		decryptBlock.append(decrypt(eblock[i],key))

	for row in decryptBlock:
		for item in row:
			decString += chr(item)

	file.write(decString)
	file.close()
	decryptelapsed = time.clock()-decrypttime
	elapsed = time.clock()-start
	print "Total Tid: " + str(elapsed)
	print "Dekrypteringstid: " + str(decryptelapsed)

if mode == "encrypt" or mode == "e":
	fileEncrypt()
elif mode == "decrypt" or mode == "d":
	fileDecrypt()
