# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        start = 0
        stop = len(s) - 1

        bool_palindrome = True

        while start < stop:
            if s[start].lower() == s[stop].lower():
                start += 1
                stop -= 1
            elif not s[start].isalnum():
                start += 1
            elif not s[stop].isalnum():
                stop -= 1
            else:
                bool_palindrome = False
                break
        return bool_palindrome




x = "A man, a plan, a canal: Panama"
# x = "race a car"

print(Solution().isPalindrome(x))