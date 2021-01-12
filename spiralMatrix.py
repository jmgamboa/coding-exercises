# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        res = []

        if not len(matrix):
            return result

        rows = len(matrix)
        row_begin = 0
        row_end = len(matrix) - 1

        cols = len(matrix[0])
        col_begin = 0
        col_end = len(matrix[0]) - 1

        while (row_begin <= row_end and col_begin <= col_begin):

            for i in range(col_begin, col_end):
                res.append(matrix[row_begin][i])
            row_begin += 1

            for i in range(row_begin, row_end):
                res.append(matrix[i][col_end])
            col_end -= 1

            if row_begin <= row_end:
                for j in range(col_end, col_begin):
                    res.append(matrix[row_end][j])

            row_end -= 1

            if col_begin <= col_end:
                for j in range(row_end, row_begin, -1):
                    res.append(matrix[j][col_begin])

            col_begin += 1

        return res





matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# col = 3
# row = 4
# array = [[0] * col for _ in range(row)]

print(Solution().spiralOrder(matrix))