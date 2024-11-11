def solution(s):
    
    one_to_bin = str(s)
    one_cnt, zero_cnt = 0, 0
    i = 0

    while one_to_bin != '1':
        # 0과 1 개수 세기
        one_cnt = one_to_bin.count('1')
        zero_cnt += one_to_bin.count('0')

        # 1 개수로 이진 변환 이전
        one = '1' * one_cnt

        # one의 길이 -> 이진수로 변환
        one_to_bin = format(len(one), 'b')
        #one_to_bin = bin(len(one)[2:]

        i += 1

    return [i, zero_cnt]