def solution(n):
    res = 0

    for i in range(n+1):
        if i%2 == 0:
            res += i
    
    return res