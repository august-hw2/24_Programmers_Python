def solution(lottos, win_nums):
    # 최고 순위 = 교집합한 값 + 0 개수
    # 최저 순위 = 교집합한 값

    rank = [6, 6, 5, 4, 3, 2, 1] # 인덱스를 이용해 순위 값 정하기

    return [rank[len(set(lottos)&set(win_nums))+lottos.count(0)], rank[len(set(lottos)&set(win_nums))]]
