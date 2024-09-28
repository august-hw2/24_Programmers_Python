def solution(name, yearning, photo):
    ans = []

    for i in photo:
        tmp = i
        cnt = 0
        for t in range(len(tmp)):
            if tmp[t] in name:
                cnt += yearning[name.index(tmp[t])]
        ans.append(cnt)

    return ans