# 문자열 나누기
def temp(arr):
    i = 0
    tmp = ""
    tmp_arr = []
    while i < len(arr):
        if arr[i] == "S" or arr[i] == "D" or arr[i] == "T":
            tmp += arr[i]
            if i+1 < len(arr) and (arr[i+1] == "*" or arr[i+1] == "#"):
                tmp += arr[i+1]
                i += 2
            else:
                i += 1
            tmp_arr.append(tmp)
            tmp = ""
        else:
            tmp += arr[i]
            i += 1

    return tmp_arr

# 나눈 문자열 대로 합 구하기
def solution(dartResult):
    arr = list(dartResult) #s,d,t를 기준으로 한 문자열 넣기
    t_arr = temp(arr) #문자열 나누는 함수 리턴 값
    res = [] # 각 문자열의 합

    for i in t_arr:
        t = 0
        if "S" in i: # 1제곱
            t = int(i[:i.index("S")])
            t = pow(t, 1)

        elif "D" in i: # 2제곱
            t = int(i[:i.index("D")])
            t = pow(t, 2)

        elif "T" in i: # 3제곱
            t = int(i[:i.index("T")])
            t = pow(t, 3)


        # 스타상, 아차상 계산
        if "*" in i and t_arr.index(i) == 0:
            t *= 2
        elif "*" in i and t_arr.index(i) != 0:
            t *= 2
            res[t_arr.index(i)-1] *= 2
        elif "#" in i:
            t *= -1

        res.append(t)

    return sum(res)

dartResult = "1D#2S*3S"
print(solution(dartResult))