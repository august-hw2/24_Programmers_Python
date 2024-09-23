def solution(a, b):
    m = max(a, b)
    n = min(a, b)
    return sum(i for i in range(n, m+1))