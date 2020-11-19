# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

# Given an array  of  integers and a number, perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.


a = [1, 2, 5, 9, 8]

def shift_left_brute(lst, n):
	n = n % len(lst)
	result = []
	# len(lst) = 5, n = 3,
	for i in range(len(lst) - n, len(lst)):
		result.append(lst[i])
	for i in range(0, len(lst) - n):
		result.append(lst[i])

	print(result)


def shift_left(lst, n):
	n = n % len(lst)
	return lst[-n:] + lst[:-n]

shift_left_brute(a, 3)



def shift_left_new(n, lst=[]):
	result = []
	new_n = n % len(lst)
	for i in range(len(lst)-n, len(lst)):
		result.append(lst[i])
	for i in range(0, len(lst)-n):
		result.append(lst[i])
	print(result)


shift_left_new(3, a)

