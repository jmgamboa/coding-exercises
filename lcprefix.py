l = ["flower","flow","flight"]


def longestCommonPrefix(l) -> str:

    prefix = ""
    temp = []
    if not strs:
        return ""
    minn = strs[0]
    for k in strs:
        if len(k)< len(minn):
            minn = k
    for i in range(len(minn)):
        count = 0
        temp = minn[i]
        for j in range(len(strs)):
            if strs[j][i] != temp:
                break
            count+=1
        if count == len(strs):
           prefix += temp
        else:
            break
    return prefix
