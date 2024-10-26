def solution(n, lost, reserve):
    # 집합 -> 차집합 이용 -> 중복제거
    re_d = set(reserve) - set(lost)
    lo_d = set(lost) - set(reserve)

    #2개 보유한 사람이 잃어버린 사람에 속하는지 확인 후 잃어버린 사람 리스트 내 요소 제거
    for i in re_d:
        if i-1 in lo_d:
            lo_d.remove(i-1)
        elif i+1 in lo_d:
            lo_d.remove(i+1)

    return n-len(lo_d)