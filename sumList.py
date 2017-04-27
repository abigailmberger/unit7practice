def sum_list(numbers) :
	""" Takes in list of numbers, adds numbers, returns sum """
	
	# Terminating Case
	if numbers == [] :
		return 0
	
	# Recursive Call
	sum = numbers[0] + sum_list(numbers[1:])
	return sum
	
	
###### Main Program ######

a = [1, 2, 3, 4, 7, 34]
print(sum_list(a))

b = [10, 56, 0, 8, 90]
print(sum_list(b))

c = [3, 2, 3, 16]
print(sum_list(c))

d = []
print(sum_list(d))

