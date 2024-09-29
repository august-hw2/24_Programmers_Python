def solution(k, m, score):
    ans = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i+m]

        if len(tmp) == m:
            ans += min(tmp)*m

    return ans