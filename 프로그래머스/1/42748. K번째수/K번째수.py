def solution(array, commands):
    tmp = []
    ans = []

    for a in commands:
        i, j, k = a
        tmp = array[i-1:j]
        tmp.sort()
        ans.append(tmp[k-1])

    return ans