#This tool can verify if a number is prime,
#putting it directly and just verify it,
#or will verify until a limit is reached
def listPrimes(limit): #Function to list primes until a defined limit
	n = 2 #start test number
	m = 1 #the number wich divides to verify if the number is prime
	rest = [] #list of the rests of the divisions
	while(n < limit): #loop to verify until the limit
		while(m<n): #verification loop
			p = n%m 
			rest = rest + [p] #add the rest of the division to the list
			count = rest.count(0) #counts how many zeros exist in the list
			m += 1 #to rise the divisor by one
			if (count > 1): #the code stops if it finds more than one zeros in the list
				break
		if (count < 2): #final verification to write that n is prime
			print(n,"is prime")
		n += 1 #raises the test number by one
		m = 1 #resets the divisor
		rest = [] #resets the list

def verifyPrime(number): #Function to verify if a number is prime
	n = number #assings the number to test to the test number
	m = 1 #the number wich divides to verify if the number is prime
	rest = [] #list of the rests of the divisions
	while(m<n): #verification loop
		p = n%m
		rest = rest + [p] #add the rest of the division to the list
		count = rest.count(0) #counts how many zeros exist in the list
		m += 1 #to rise the divisor by one
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
    print("What limit number do you want?")
    limit = int(input()) #receives the limit number
    listPrimes(limit) #calls the function
if (choice == 2):
    print("What number do you want to verify?")
    number = int(input()) #receives the number to test
    verifyPrime(number) #calls the function
if (choice != 1 and choice !=2):
	print("Invalid option")