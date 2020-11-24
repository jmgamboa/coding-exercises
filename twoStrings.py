# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

# twoStrings has the following parameter(s):

# s1, s2: two strings to analyze .
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.


s1 = 'a'
s2 = 'b'

s1 = 'art'
s2 = 'artistic'

s1 = 'hello'
s2 = 'world'

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	result = 'NO'
	for i in s1:
		if i in s2:
			result = 'YES'
	print(result)

twoStrings(s1, s2)


