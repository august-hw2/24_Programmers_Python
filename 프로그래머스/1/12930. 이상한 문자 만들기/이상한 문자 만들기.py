def solution(s):
    ans = ""

    for i in s.split(" "):
        t = ""
        for j in range(len(i)):
            if j%2: #홀수인 경우
                t += i[j].lower()
            else: #짝수인 경우
                t += i[j].upper()
        #리턴할 변수에 저장
        ans += t
        ans += " "

    return ans[:-1]