def solution(s):
    tmp = sorted(list(s))
    
    res = ""
    
    for i in tmp:
        if tmp.count(i) == 1:
            res += i

    return res