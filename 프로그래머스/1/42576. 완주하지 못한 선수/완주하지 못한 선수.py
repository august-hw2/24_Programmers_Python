def solution(participant, completion):
    
    #해시 함수 이용 코드
    hashDict = {}
    sumHash = 0
    
    #hash 함수 이용 -> 전체 해시 값
    for i in participant:
        hashDict[hash(i)] = i
        sumHash += hash(i)
        
    #해시 총 값 - 완주한 리스트의 해시 값 = 완주하지 못한 해시 값
    for j in completion:
        sumHash -= hash(j)

    return hashDict[sumHash]

    """ 
    <- 시간 초과 ->
    # 리스트명 = 리스트명 -> 주소가 복사되어 그 자체 복제됨
    # 리스트명 = 리스트명[:] or list(리스트명)으로 새로운 객체 생성 후 값 저장
    res = participant[:]

    for i in participant:
        if i in completion:
            res.remove(i)
            completion.remove(i)

    return res[0]
    """