n = 2
rest = []
primes = [1]
count = 0
while(n <= 3001):
	i = 0
	m = primes[i]
	while(m<n):
		p = n%m
		rest = rest + [p]
		count = rest.count(0)
		i += 1
		if((i+1) > len(primes)):
			break
		m = primes[i]
		if (count > 1):
			break
	if (count == 1):
		print(n,"is prime")
		primes = primes + [n]
	n += 1
	rest = []