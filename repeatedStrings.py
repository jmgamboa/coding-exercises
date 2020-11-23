# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

# For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

s = 'aba'
n = 10
# e o 7
# because abaabaabaa




# s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
# n = 736778906400
# e o 7

def repeatedString(s, n):
	if len(s) == 1 and s == 'a':
		return n

	repeat_string = s
	while len(repeat_string) < n:
		repeat_string += repeat_string

	count = 0
	for i in repeat_string[0:n]:
		if i == 'a':
			count += 1


	return count


print(repeatedString(s, n))