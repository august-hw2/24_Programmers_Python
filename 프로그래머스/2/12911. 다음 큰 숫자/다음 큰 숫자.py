def solution(n):
    answer = 0

    # 2진수로 변환
    bin_n = bin(n)[2:]

    # 1의 개수 세기
    one_cnt = bin_n.count('1')

    for i in range(n+1, 1000001):
        if bin(i)[2:].count('1') == one_cnt:
            return i