import math
def generate_prime_numbers(n):
	
	if isinstance(n, str):
		return "Only numbers accepted"
	if not isinstance(n, int):
		return "Only numbers accepted"
	if n <2:
		return "only numbers greater than 2 accepted"

	else:
		prime_numbers= []
		for num in range(2,n+1):
		    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
		    	prime_numbers.append(num)
		return prime_numbers 