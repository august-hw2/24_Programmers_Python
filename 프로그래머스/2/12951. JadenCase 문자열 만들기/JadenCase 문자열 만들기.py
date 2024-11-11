def solution(s):

    s = s.lower()
    tmp = list(s)

    if tmp[0].isalpha():
        tmp[0] = tmp[0].upper()

    for i in range(len(tmp)):
        if i+1 < len(tmp) and tmp[i] == ' ' and tmp[i+1] != ' ':
            tmp[i+1] = tmp[i+1].upper()

    return ''.join(tmp)