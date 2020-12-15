# https://leetcode.com/problems/length-of-last-word/submissions/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        chars = len(s)

        if not chars:
            print('got here')
            return 0
        words = []
        curr_word = ""
        for idx, i in enumerate(s):
            curr_word += i
            if idx == (len(s)-1) or s[idx+1] == " ":
                cleaned = curr_word.replace(" ", "")
                if cleaned:
                    words.append(cleaned)
                    curr_word = ""
        if words:
            return len(words[-1])
        else:
            return 0


print(Solution().lengthOfLastWord("a "))