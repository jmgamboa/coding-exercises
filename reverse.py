s1 = '-123'
s2 = '120'

def reversed(x: int) -> int:
    result = ''
    negative = False
    st = str(x)
    if "-" in st:
        st = st.replace('-', '')
        negative = True
    for i in st[::-1]:
        result += i
    if negative:
        final_result = "-" + result
    else:
        final_result = result
    return int(final_result)


print(reversed(s2))