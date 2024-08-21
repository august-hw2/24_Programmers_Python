def solution(my_string):
    res = []
    my_string = list(my_string)
    
    for i in my_string:
        if i not in res:
            res.append(i)
    
    return ''.join(res)