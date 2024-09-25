def solution(s, n):
    
    tmp = list(s)
    ans = ""
    
    for i in tmp:

        if i.islower():
            ans += chr((ord(i)-ord('a')+n) % 26 + ord('a'))
        elif i.isupper():
            ans += chr((ord(i)-ord('A')+n) % 26 + ord('A'))
        else:
            ans += " "

    return ans