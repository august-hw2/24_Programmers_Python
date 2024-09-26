def solution(s):
    ans, tmp = "", ""
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    s_list = list(s)

    for i in range(len(s_list)):
        if s_list[i].isdecimal():
            ans += s_list[i]
        else:
            tmp += s_list[i]
            if tmp in dic:
                ans += dic[tmp]
                tmp = ""  # 초기화

    return int(ans)