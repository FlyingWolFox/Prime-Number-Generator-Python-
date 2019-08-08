#This tool can verify if a number is prime,
#putting it directly and just verify it,
#or will verify until a limit is reached

def listPrimes(limit): #Function to list primes until a defined limit
	n = 2 #start test number
	rest = [] #list of the rests of the divisions
	primes = [1] #list of primes.Updates itself as the function runs and make the division occur only with a prime[note 1 for more info]
	count = 0 #count initialization
	if (limit != 0):
		while(n <= limit): #loop to verify until the limit
			i = 0 #used to get am iten of the primes list
			m = primes[i] #gets the firt item in the list primes (1)
			while(m<n): #verification loop
				p = n%m #gets the rest
				rest = rest + [p] #add the rest of the division to the list
				count = rest.count(0) #counts how many zeros exist in the list
				i += 1 #to set m to the next prime in the list 
				if(((i+1) > len(primes)) or (count > 1)): #this stops if exists more than one zero in the list and if the i isn't out of the range of the list
					break
				m = primes[i] #gets the next number in the list
			if (count == 1): #final verification to write that n is prime
				print(n,"is prime")
				primes = primes + [n] #adds the prime found to the list
			n += 1 #raises the test number by one
			rest = [] #resets the rest list
	if (limit == 0):
		while(n > 0): #loop to verify until the limit
			i = 0 #used to get am iten of the primes list
			m = primes[i] #gets the firt item in the list primes (1)
			while(m<n): #verification loop
				p = n%m #gets the rest
				rest = rest + [p] #add the rest of the division to the list
				count = rest.count(0) #counts how many zeros exist in the list
				i += 1 #to set m to the next prime in the list 
				if(((i+1) > len(primes)) or (count > 1)): #this stops if exists more than one zero in the list and if the i isn't out of the range of the list
					break
				m = primes[i] #gets the next number in the list
			if (count == 1): #final verification to write that n is prime
				print(n,"is prime")
				primes = primes + [n] #adds the prime found to the list
			if n == 2:
				n += 1 #makes the test number odd
			if n != 2:
				n += 2 #maintain the test number odd
			rest = [] #resets the rest list
		
def verifyPrime(number): #Function to verify if a number is prime
	n = number #assings the number to test to the test number
	m = 1 #the number wich divides to verify if the number is prime
	rest = [] #list of the rests of the divisions
	while(m<n): #verification loop
		p = n%m
		rest = rest + [p] #add the rest of the division to the list
		count = rest.count(0) #counts how many zeros exist in the list
		if m == 2:
			m += 1 #makes the divisor odd
		else:
			m += 2 #rise the divisor maintining it odd
		if (count > 1): #here the code stops if it finds there are more than one zeros in the list (great optimization)
			print(n,"ins't prime")
			break
	if (count < 2): #final verification to write that n is prime
		print(n, "is prime")

print("Do you want to:")
print("1-List Prime until a certain limit")
print("2-Verify if a number is prime")
print("Type your option:")
choice = int(input()) #receives the option selected
if (choice == 1):
    print("What limit number do you want? (type 0 to not set any limit)")
    limit = int(input()) #receives the limit number
    listPrimes(limit) #calls the function
if (choice == 2):
    print("What number do you want to verify?")
    number = int(input()) #receives the number to test
    verifyPrime(number) #calls the function
if (choice != 1 and choice !=2):
	print("Invalid option")
	

	
#Note 1: "In number theory, the fundamental theorem of arithmetic,
#also called the unique factorization theorem or the unique-prime-factorization theorem,
#states that every integer greater than 1 either is a prime number itself
#or can be represented as the product of prime numbers and that, moreover,
#this representation is unique, up to (except for) the order of the factors"
#this is used to make the test numbers(n) just be divided by primes,
#because of the theorem, if a number isn't a multiple of a prime number,
#it's is itself a prime. This is used here to gain a giant boost, making
#divisions with few numbers, ignoring numbers that are multiple of others.