from random import randint

def gcd(a,b):
	while b != 0:
		a, b = b, a % b
	return a

def give_primitive_root(modulo):
	roots = []
	required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
	for g in range(1, modulo):
		actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
		if required_set == actual_set:
			roots.append(g)
	return roots[0]

def main():
	n = 17
	g = give_primitive_root(n)
	xa = randint(1, n)
	ya = pow(g, xa, n)
	xb = randint(1, n)
	yb = pow(g, xb, n)
	k = pow(ya, xb, n)
	print "Secret key: ", k

if __name__ == "__main__":
	main()