def solution(n):
    s = ""

    for i in range(n):
        if i%2:
            s += "박"
        else:
            s += "수"
    return s