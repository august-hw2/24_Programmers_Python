def solution(n, arr1, arr2):
    a, b = [], []
    ans = []

    for i in arr1:
        if len(bin(i)[2:]) != n:
            tmp = "0"*(n-len(bin(i)[2:]))
            a.append(list(tmp+bin(i)[2:]))
        else:
            a.append(list(bin(i)[2:]))

    for j in arr2:
        if len(bin(j)[2:]) != n:
            tmp = "0" * (n - len(bin(j)[2:]))
            b.append(list(tmp + bin(j)[2:]))
        else:
            b.append(list(bin(j)[2:]))

    for x in range(n):
        tmp_arr = []
        for y in range(n):
            if a[x][y] == "0" and b[x][y] == "0":
                tmp_arr.append(' ')
            else:
                tmp_arr.append('#')
        ans.append(''.join(tmp_arr))

    return ans