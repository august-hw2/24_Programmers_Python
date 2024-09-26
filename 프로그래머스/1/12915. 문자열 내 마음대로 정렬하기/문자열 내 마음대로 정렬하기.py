def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            a, b = strings[i], strings[j]
            if a[n] > b[n]:
                strings[i], strings[j] = b, a
            elif a[n] == b[n]:
                if a > b:
                    strings[i], strings[j] = b, a
        
    return strings