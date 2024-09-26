def solution(s):
    s_list = list(s)
    arr = []
    ans = []

    for i in range(len(s_list)):
        if s_list[i] not in arr:
            arr.append(s_list[i])
            ans.append(-1)
        else:
            tmp = str(''.join(s_list[:i]))
            ans.append(i - tmp.rindex(s_list[i]))

    return ans