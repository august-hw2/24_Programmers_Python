def solution(s):
    if len(s)%2: #홀수인 경우
        return s[len(s)//2]
    else: #짝수인 경우
        return s[len(s)//2-1:len(s)//2+1]