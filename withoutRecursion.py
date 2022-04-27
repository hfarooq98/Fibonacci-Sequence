#This code gives nth number in fibonacci series - {0,1,1,2,3,5,......}.
#Without Recursion

import math

def fibo(n):
	phi = (1 + math.sqrt(5)) / 2

	return round(pow(phi, n) / math.sqrt(5))
	

n = int(input("For nth Fibonacci Number, Enter n: "))
print(fibo(n))
