def solution(my_string, n):
    tmp = list(my_string)
    
    res = ""
           
    for i in tmp:
        for j in range(n):
            res += i
           
    return res