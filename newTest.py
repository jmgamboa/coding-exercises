


# for lst = [1, 2, 3, 5, 9] and n = 3
def shift_left_new(n, lst):
	for i in range(0, n):
		val = lst[i]
		del lst[i]
		lst.append(i)
	for i in lst:
		print(i)
































# for lst = [1, 2, 3, 5, 9] and n = 3
def shift_left_brute(lst, n):
	n = n % len(lst)

	result = []
	# len(lst) = 5, n = 3,
	# iterate from n to end of list and append append
	for i in range(0, len(lst) - n):
		result.append(lst[i])
	# append the shift
	for i in range(len(lst) - n, len(lst)):
		result.append(lst[i])
	# append the

	print(result)




















# for lst = [1, 2, 3, 5, 9] and n = 3
def shift_left(lst, n):
	n = n % len(lst)
	newlist = lst[-n:] + lst[:-n]
	return newlist








