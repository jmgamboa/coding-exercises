# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, g: str) -> int:
        n = len(g)

        chars = []
        ans = 0
        i = 0
        j = 0

        while (i < n and j < n):

            if g[j] not in chars:
                chars.append(s[j])
                j += 1
                ans = max(ans, j-1)
            else:
                chars.remove(s[i])
                i += 1
        return ans

# class Solution:
#     def lengthOfLongestSubstring(self, g: str) -> int:
#         n = len(g)
#         ans = 0
#         # mp stores the current index of a character
#         mp = {}

#         i = 0
#         # try to extend the range [i, j]
#         for j in range(n):
#             if g[j] in mp:
#                 i = max(mp[g[j]], i)

#             ans = max(ans, j - i + 1)
#             mp[g[j]] = j + 1

#         return ans

class Solution:
    def lengthOfLongestSubstring(self, g: str) -> int:
        num = len(g)
        chars = []

        i = 0
        j = 0
        res = 0

        while (i < num and j < num):
            if g[j] not in chars:
                chars.append(g[j])
                j += 1
                res = max(res, j-i)
            else:
                chars.remove(g[i])
                i += 1

        return res


# s = "bwf"
# s = "bbbbb"
s = "aabacgd" # 5
# s = "abcdeafbdgcbb" # answer is 7
print(Solution().lengthOfLongestSubstring(s))