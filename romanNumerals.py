
# https://leetcode.com/problems/roman-to-integer/


s1 = "III"
s2 = "IV"
s3 = "LVIII"

def romanToInt(s: str) -> int:

    rMap2 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    for idx, v in enumerate(s):
        if idx == len(s)-1:
            total += rMap2[v]
            continue
        curr = rMap2[v]
        next_v = rMap2[s[idx+1]]

        if curr < next_v:
            total -= curr
        else:
            total += rMap2[v]
    return total


print(romanToInt(s3))
