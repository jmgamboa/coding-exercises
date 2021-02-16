# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        step = 1
        end = len(s)
        longest_substring = s[0]

        while start < end:
            substring = s[start]
            count = 0
            for i in s[step:end]:
                substring += i
                if substring == substring[::-1] and \
                 len(substring) > len(longest_substring):
                    longest_substring = substring
            step += 1
            start += 1
        return longest_substring







s = "babad"
s1 = "cbbd"
s2 = "bb"
s3 = "ccc"

print(Solution().longestPalindrome(s2))