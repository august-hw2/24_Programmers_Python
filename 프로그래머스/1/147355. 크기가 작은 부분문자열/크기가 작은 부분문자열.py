def solution(t, p):
    tmp = []
    cnt = 0

    for i in range(len(t)-len(p)+1):
        tmp.append(t[i:i+len(p)])

    for j in tmp:
        if int(j) <= int(p):
            cnt += 1

    return cnt