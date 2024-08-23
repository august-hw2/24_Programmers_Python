def solution(s):
    s = list(s.split(' '))

    while True:
        if 'Z' not in s:
            return sum(int(i) for i in s)
            break
        else:
            del s[s.index('Z')-1:s.index('Z')+1]