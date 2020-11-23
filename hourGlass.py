"""Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description"""



w, h = 6, 6;
matrix = [[0 for x in range(w)] for y in range(h)]

# not matrix[0][x] all
matrix[1][1] = 2
matrix[1][2] = 5
matrix[1][3] = 7
matrix[1][4] = 8

matrix[2][1] = 1
matrix[2][2] = 2
matrix[2][3] = 5
matrix[2][4] = 8

matrix[3][1] = 3
matrix[3][2] = 5
matrix[3][3] = 7
matrix[3][4] = 9

matrix[4][1] = 0
matrix[4][2] = 0
matrix[4][3] = 0
matrix[4][4] = 0

# not matrix[5][x] all


# not matrix[0][0]
# not matrix[1][0]
# not matrix[2][0]
# not matrix[3][0]
# not matrix[4][0]
# not matrix[5][0]

# not matrix
# not matrix[0][5]
# not matrix[1][5]
# not matrix[2][5]
# not matrix[3][5]
# not matrix[4][5]
# not matrix[5][5]


def calculateHourGlass(matrix, i, j):
	# i = 1 j = 1
	vertex = matrix[i][j]

	total = 0

	total += (matrix[i][j] + matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1])
	total += (matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1])
	return total


hourglasstotal = -90

for i in range(1,5):

	for j in range(1, 5):

		currTotal = calculateHourGlass(matrix, i, j)
		print(f' curr total = {currTotal}')
		if currTotal > hourglasstotal:
			hourglasstotal = currTotal
print(f'final val {hourglasstotal}')

for i in matrix:
	print(i)