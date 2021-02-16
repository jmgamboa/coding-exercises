# https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        pointer = 0

        str_count = 0
        index_of = 0

        for idx, i in enumerate(haystack):

            if i == needle[pointer]:
                if str_count == 0:

                    index_of = idx
                str_count += 1
                pointer += 1

                if len(needle) == str_count:
                    return index_of
            else:
                str_count = 0
                pointer = 0

        return -1



# haystack = "hello"
# needle = "ll"

# haystack = "aaaaa"
# needle = "bba"

# haystack = "a"
# needle = "a"

haystack = "mississippi"
needle = "issip"

print(Solution().strStr(haystack, needle))