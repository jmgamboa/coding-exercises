# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n-1)
        count, prev, res = 0, s[0], []
        for ch in s:
            if ch == prev:
                count += 1
            else:
                res.append(f'{str(count)}{prev}')
                prev, count = ch, 1

        res.append(f'{str(count)}{prev}')
        return ''.join(res)