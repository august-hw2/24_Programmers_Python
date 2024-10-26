def solution(s):
    
    arr = list(s) #문자열 -> 리스트로
    ans_arr = [] #분리된 문자열 저장 리스트

    i = 0
    x, not_x = "", ""

    while i < len(arr):

        if x == "":
            tmp = arr[i]
        if tmp == arr[i]:
            x += arr[i]
        else:
            not_x += arr[i]

        if len(x) == len(not_x):
            ans_arr.append(x+not_x)
            x, not_x = "", ""

        i += 1

    if len("".join(ans_arr)) != len(s):
        ans_arr.append(s.lstrip("".join(ans_arr)))
    elif s.lstrip("".join(ans_arr)) != "":
        pass

    return len(ans_arr)