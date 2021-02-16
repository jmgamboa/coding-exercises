# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_unique_substring, curr_string = ""

        start = 0
        step = 1
        uniques = list()

        while start < len(s) and step < len(s):

            curr_string += s[step]

            if s[start] in uniques:
                start += 1

                step += 1
                uniques = list()
            else:
                step += 1
                uniques.append(s[start])
                if len(curr_string) > len(longest_unique_substring):
                    longest_unique_substring = curr_string + s[step]

            if s[step] in uniques:
                start += 1
                step += 1
                uniques = list()
            else:
                step += 1
                uniques.append(s[start])


 s = "abcabcbb"

Solution().lengthOfLongestSubstring(s)