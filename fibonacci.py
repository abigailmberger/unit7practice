def fibonacci(numbers, term) :
	""" Takes in two numbers in a list to start Fibonacci sequence, and returns nth term """
	
	# Terminating Case
	if len(numbers) == term :
		return numbers[-1]
	
	# Recursive Call
	numbers.append(numbers[-1] + numbers[-2])
	return fibonacci(numbers, term)
	
	
###### Main Program ######

print(fibonacci([1, 1], 4))	
print(fibonacci([1, 1], 14))	
print(fibonacci([5, 8], 2))
print(fibonacci([2, 6], 12))
	