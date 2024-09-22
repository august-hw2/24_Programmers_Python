def solution(n):
    ans = 0

    for i in list(str(n)):
        ans += int(i)

    return ans