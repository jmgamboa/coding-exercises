# navigate from a matrix of N by N from left to right and find the sum
# navigate from right to left and find the sum


matrix = [[0]*3 for i in range(3)]

rows = len(matrix)
cols = len(matrix[0])

print(f'rows {rows}')
print(f'cols {cols}')

# left to right diagonal
# start = matrix[0][0]
# middle = mamtrix[1][1]
# end = matrix[2][2]

# right to left diagnol
# start = matrix[0][2]
# middle = matrix[1][1]
# end = matrix[2][0]


matrix[0][0] = 5
matrix[0][2] = 3
matrix[1][1] = 7
matrix[2][0] = 1
matrix[2][2] = 9

def sumLeftToRight(matrix):
	total = 0
	for i in range(0, rows):
		total += matrix[i][i]
	print(f'the sum from left to right is {total}')


def sumRightToLeft(matrix):
	total = 0
	colCounter = cols - 1
	for i in range(0, rows):
		total += matrix[i][colCounter]
		colCounter -= 1
	print(f'the sum from right to left is {total}')


print('this is the matrix')
for i in matrix:
	print(i)

sumRightToLeft(matrix)
sumLeftToRight(matrix)


