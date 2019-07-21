n = 2
m = 1
rest = []
print ("2 is prime")
while(n < 1000):
	if (n%2 != 0 and n%5 != 0):
		while(m<n):
			p = n%m
			rest = rest + [p]
			count = rest.count(0)
			m += 1
		if (count < 2):
			print(n,"is prime")
	n += 1
	m = 1
	rest = []
