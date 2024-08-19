def solution(s1, s2):
    
    res = 0
    
    for i in s1:
        for j in s2:
            if i == j:
                res += 1
    return res