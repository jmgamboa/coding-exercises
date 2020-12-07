# https://leetcode.com/problems/valid-parentheses/
class Solution:
	def isValid(self, seq: str) -> bool:
		match = {'{': '}', '(': ')', '[': ']'}
		stack = []
		for i in seq:
			if i == '{' or i == '(' or i == '[':
				stack.append(i)
			elif not stack:
				return False
			elif i == '}' or i == ')' or i == ']':
				peek = stack[-1]
				if match[peek] == i:
					del stack[-1]
				else:
					return False
		return not bool(stack)


s1 = "()"
s2 = "()[]{{}}"
s3 = "(]"
s4 = "([)]"
s5 = "{{[]}}"
s6 = "(("


print(Solution().isValid(s6))