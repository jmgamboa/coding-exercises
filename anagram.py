
def solution(A, B):
    if len(A) == 0 or len(B) == 0:
        return max(len(A), len(B))

    letter_count = 0
    A_dict = {}
    B_dict = {}

    for i in A:
        if i not in A_dict:
            A_dict[i] = 1
        else:
            A_dict[i] += 1
    for i in B:
       if i not in B_dict:
           B_dict[i] = 1
       else:
           B_dict[i] += 1

    for k, v in A_dict.items():
        if k not in B_dict:
            letter_count += v
        else:
            if v > B_dict[k]:
                letter_count += v - B_dict[k]

    for k, v in B_dict.items():
        if k not in A_dict:
            letter_count += v
        else:
            if v > A_dict[k]:
                letter_count += v - A_dict[k]

    return letter_count


print(solution('apple', ''))

# In [32]: def anagram(s1, s2):
#     ...:     _map = {}
#     ...:     for i in s1:
#     ...:         if i not in _map:
#     ...:             _map[i] = 0
#     ...:         _map[i] += 1
#     ...:     for i in s2:
#     ...:         if i not in _map:
#     ...:             _map[i] = 1
#     ...:         else:
#     ...:             _map[i] -= 1
#     ...:             if _map[i] == 0:
#     ...:                 del _map[i]
#     ...:     return len(_map)
#     ...:
