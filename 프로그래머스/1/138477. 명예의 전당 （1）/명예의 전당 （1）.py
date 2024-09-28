def solution(k, score):
    tmp = [] #k값 만큼 저장할 리스트
    ans = [] #리턴할 리스트

    for i in range(len(score)):
        tmp.append(score[i])
        if len(tmp) > k:
            tmp.remove(min(tmp))

        ans.append(min(tmp))
    
    return ans