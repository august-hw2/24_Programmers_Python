# 1) +k
# 2) (지금까지 온 거리) * 2 의 위치임 (이동 거리 의미x)
# 즉, %2한 값이 0이 아닐 때 1번 방법으로 이동

def solution(n):
    ans = 0

    while n != 0:
        if n%2 == 0:
            n/=2
        else:
            n -= 1
            ans += 1

    return ans