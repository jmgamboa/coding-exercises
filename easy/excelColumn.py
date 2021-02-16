# https://leetcode.com/problems/excel-sheet-column-title/
import math

class Solution:
    def convertToTitle(self, n: int) -> str:
        col_dict = {
           '1':'A',
           '2':'B',
           '3':'C',
           '4':'D',
           '5':'E',
           '6':'F',
           '7':'G',
           '8':'H',
           '9':'I',
            '10':'J',
            '11':'K',
            '12':'L',
            '13':'M',
            '14':'N',
            '15':'O',
            '16':'P',
            '17':'Q',
            '18':'R',
            '19':'S',
            '20':'T',
            '21':'U',
            '22':'V',
            '23':'W',
            '24':'X',
            '25':'Y',
            '26':'Z'
        }

        if n <= 26:
            return col_dict[str(n)]

        else:
            remainder = n % 26
            prefix = math.floor(n / 26)
            if remainder:
                col = col_dict[str(prefix)] + col_dict[str(remainder)]
            else:
                col = col_dict[str(prefix-1)] + 'Z'
            return col


# 28 = AB
# 52 = AZ
# 703 = ZX

n = 703
# expected output = AZ
print(Solution().convertToTitle(n))