# https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # same as calculating fibonacci(n)
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1
        curr = 2

        for i in range(2, n):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr