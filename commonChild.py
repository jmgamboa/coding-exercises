# https://www.hackerrank.com/challenges/common-child/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign

s1 = 'SHINCHAN'
s2 = 'NOHARAAA'


def commonChild(s1, s2):

    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)

    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr,prev

    return prev[-1]



commonChild(s1, s2)