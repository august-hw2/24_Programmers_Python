def solution(i, j, k):
    res = 0

    for i in range(i, j+1):
        tmp = list(map(int, str(i)))
        if k in tmp:
            res += tmp.count(k)
            
    return res
            