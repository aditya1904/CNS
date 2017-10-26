#!/usr/bin/env python
#
# Copyright (c) 2017 by Aditya Malu adityamalu1@gmail.com. All Rights Reserved.
#

## Sample Program to show the working of RSA cryptosystem ##

from random import *

max_of_p_q = 10000

def is_prime(num):
	"""Returns True if the number is prime
	else False."""
	if num == 0 or num == 1:
		return False
	for x in range(2, num//2):
		if num % x == 0:
			return False
	else:
		return True

def gcd(a, b):
	"""Calculate the Greatest Common Divisor of a and b.
	Unless b==0, the result will have the same sign as b (so that when
	b is divided by it, the result comes out positive).
	"""
	while b:
		a, b = b, a%b
	return a

def lcm(a, b):
	return (a*b) / gcd(a, b)

def is_coprime(a, b):
	if gcd(a, b) == 1:
		return True
	else:
		return False

def mod_mul_inv(a, num):
	''' This is a simple method. Extended Euclidean Algorithm is recommended for
		modular multiplicative inverse'''
	for i in xrange(num):
		if (a*i)%num == 1:
			return i
	return 0

def generate_keys():
	p, q = 1, 1
	while(not is_prime(p)):
		p = randint(1, max_of_p_q)
	while(not is_prime(q) and p!=q):
		q = randint(1, max_of_p_q)
	n = p * q
	lambda_n = lcm(p-1, q-1)
	e = randint(1, lambda_n)
	while(not is_coprime(e, lambda_n)):
		e = randint(1, lambda_n)
	d = mod_mul_inv(e, lambda_n)
	public_key = (e, n)
	private_key = (d, n)
	return public_key, private_key

def encrypt(public_key, m):
	e = public_key[0]
	n = public_key[1]
	c = pow(m, e, n)
	return c

def decrypt(private_key, ciphertext):
	d = private_key[0]
	n = private_key[1]
	plaintext = pow(ciphertext, d, n)
	return plaintext

def main():
	public_key, private_key = generate_keys()
	print "Public Key (e, n) : ", public_key
	print "Private Key (d, n) : ", private_key
	m = int(raw_input("Enter message num: "))
	ciphertext = encrypt(public_key, m)
	print "Encrypted: ", ciphertext
	plaintext = decrypt(private_key, ciphertext)
	print "Decrypted: ", plaintext
	assert m == plaintext, "Message and deciphered text don't match"

if __name__ == "__main__":
	main()