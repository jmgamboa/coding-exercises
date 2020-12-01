# Count how many palindromes in a given string


def palindromeCount(s):

	tally = 0
	substring = ''
	for i in s:
		substring += i
		if substring == reversed(substring):
			tally += 0
	return tally()



s = '10101'
# has 3 10101, 101, 010
print(palindromeCount)