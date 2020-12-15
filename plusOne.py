# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        last_digit = digits[-1]
        result = []
        if last_digit != 9:
            digits[-1] += 1
            return digits
        else:
            carry = 1
            for idx, i in enumerate(reversed(digits)):
                val = i + carry
                if val > 9:
                    result.insert(0, 0)
                    carry = 1
                else:
                    result.insert(0, val)
                    carry = 0
        if carry:
            result.insert(0, carry)
        return result



digits = [8,9,9,9]
print(Solution().plusOne(digits))