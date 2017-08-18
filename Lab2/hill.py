#!/usr/bin/env python
from string import punctuation
import sys

def remove_punctuation(message):
	message = message.translate(None, punctuation); #removing !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
	message = ''.join(message.split()) #removing tabs, spaces, newlines
	return message.lower()

def padthemessage(message):
	if(len(message)%3 == 0):
		return message
	else:
		short = 3 - len(message)%3
		for i in range(short):
			message += 'x'				#appending x to make message length a multiple of 5
		return message

def display_format(message):
	'''	Print the final encoded message in blocks of five letters and ten blocks per line.
		The last line may be shorter than five blocks, and the last block may be shorter
		than five letters. '''
	output = []
	enc = ""
	while message:
		output.append(message[:5])
		message = message[5:]
	for index, block in enumerate(output):
		if((index + 1) % 10 == 0):
			enc = enc + block + "\n"
		else:
			enc = enc + block + " "
	return enc

def matrix_multiply(matrix_1, matrix_2):
	if(len(matrix_1[0]) == len(matrix_2)): ##Condition for matrix multiplication.
		rows = len(matrix_1)
		cols = len(matrix_2[0])
		cipher_matrix = [[0]]*rows
		for i in range(rows):
			row = []
			for j in range(cols):
				res = 0
				for k in range(len(matrix_2)):
					res += (matrix_1[i][k] * matrix_2[k][j])
				row.append(chr(ord('a') + res%26))
			cipher_matrix[i] = row
		cipher_matrix = [list(x) for x in zip(*cipher_matrix)] ## transpose of a matrix
		return cipher_matrix
	else:
		print "Matrices cannnot be multiplied..."
		sys.exit(0);

def generate_matrix(content, rows, cols):
	matrix = [[0]]*rows	 #initializing a matrix with zeros
	k = 0
	for i in range(rows):
		row = []
		for j in range(cols):
			row.append(ord(content[k])-ord('a'))
			k+=1
		matrix[i] = row
	return matrix

def encrypt(message, key):
	key_matrix = generate_matrix(key, 3, 3)
	message_matrix = generate_matrix(message, len(message)/3 , 3)
	message_matrix = [list(x) for x in zip(*message_matrix)] ## transpose of a matrix
	cipher_matrix = matrix_multiply(key_matrix, message_matrix)
	ciphertext = ''.join([ch for row in cipher_matrix for ch in row])
	ciphertext = display_format(ciphertext)
	return ciphertext

def main():
	try:
		case = int(raw_input("1 to encrypt plain_text\n2 to decrypt ciphertext\nEnter option : "))
		if(case == 1):
			k = raw_input("Enter key (exactly 9 chars): ")
			if(len(k) != 9):
				print("Enter key of size 9 only...")
				sys.exit(0)
			message = padthemessage(remove_punctuation(raw_input("Message[Plain Text]: ")))
			encrypted_message = encrypt(message, k)
			print "Encrypted Message..."
			print encrypted_message
			sys.exit(0)
		if(case == 2):
			encrypted_message = raw_input("Ciphertext: ")
			#decrypt(encrypted_message)
			sys.exit(0)
		else:
			print "Wrong option"
			sys.exit(0)
	except KeyboardInterrupt:
		print "\nClosing the program..."
		sys.exit(0)

if __name__ == '__main__':
	main()
