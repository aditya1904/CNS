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
