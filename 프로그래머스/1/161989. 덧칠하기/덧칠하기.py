def solution(n, m, section):
    ans, painted = 0, 0

    for s in section:
        if s>painted:
            painted = s+m-1
            ans += 1
    return ans