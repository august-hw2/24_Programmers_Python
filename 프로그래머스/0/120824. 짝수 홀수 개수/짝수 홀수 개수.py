def solution(num_list):
    
    res = [0, 0]
    
    for i in range(len(num_list)):
        if num_list[i]%2: #홀수
            res[1] += 1
        else:
            res[0] += 1
    return res
        