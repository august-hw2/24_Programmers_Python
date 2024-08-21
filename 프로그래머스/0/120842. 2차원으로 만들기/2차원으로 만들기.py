def solution(num_list, n):
    res = []

    for i in range(0, len(num_list), n):
        tmp = []
        for j in range(i, i+n):
            tmp.append(num_list[j])
        res.append(tmp)
        
    return res