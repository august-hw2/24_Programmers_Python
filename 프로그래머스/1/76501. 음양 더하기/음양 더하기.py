def solution(absolutes, signs):
    ans = 0

    for i, j in enumerate(absolutes):
        if signs[i] == True:
            ans += j
        else:
            ans -= j

    return ans