def multiply(number, otherNumber) :
	""" Takes two integers and returns product """
	
	if otherNumber == 0 :
		return 0
		
	product = number + multiply(number, otherNumber - 1)
	return product
	
	
	
print(multiply(4, 5))
print(multiply(1, 2))
print(multiply(4, 1))
print(multiply(10, 8))
print(multiply(0, 6))
print(multiply(3, 0))