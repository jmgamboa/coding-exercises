# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_prefix = 4 - len(a)
        b_prefix = 4 - len(b)
        if a_prefix:
            a = (a_prefix * "0") + a
        if b_prefix:
            b = (b_prefix * "0") + b


        final = ""
        carry = 0
        rev_a = reversed(a)
        rev_b = reversed(b)
        for i, j in zip(rev_a, rev_b):
            val = int(i) + int(j) + carry
            if val == 3:
                final += "1"
                carry = 1
            if val == 2:
                final += "0"
                carry = 0
            elif val == 1:
                final += "1"
                carry = 0
            elif val == 0:
                final += "0"
                carry = 0

        print(final)



a = "11"
b = "1"

print(Solution().addBinary(a,b))


# 0011
# 0001

# 0100


# 0011
# 0011

# 0110






