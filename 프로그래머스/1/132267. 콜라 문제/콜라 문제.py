def solution(a, b, n):
    x = 0
    ans = 0

    while n >= a:
        m=n%a
        x = n//a
        n = x*b+m
        ans += x*b

    return ans