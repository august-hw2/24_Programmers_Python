def solution(num):
    cnt = 0

    while True:

        if num == 1:
            return cnt

        if cnt == 500:
            return -1

        if num%2: #홀수인 경우
            num = num * 3 +1
            cnt += 1
        else: #짝수인 경우
            num //= 2
            cnt += 1