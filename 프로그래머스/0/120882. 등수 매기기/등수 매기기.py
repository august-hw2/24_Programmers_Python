def solution(score):
    tmp = []
    
    #평균 값 저장
    for i in score:
        tmp.append(sum(i))

    #평균 값 순서(오름차순) 정렬
    res = sorted(tmp, reverse=True)
    
    #정렬한 배열의 인덱스를 이용해서 기존 배열의 값과 일치하는 지 확인
    return [res.index(k)+1 for k in tmp]