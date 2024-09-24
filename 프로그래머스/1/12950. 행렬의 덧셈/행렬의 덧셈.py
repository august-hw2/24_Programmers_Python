def solution(arr1, arr2):
    tmp, ans = [], []

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        ans.append(tmp)
        tmp = []

    return ans