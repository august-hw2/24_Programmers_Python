def solution(lines):
    a, b, c = [], [], []

    for i in range(lines[0][0], lines[0][1]):
        a.append(i)

    for i in range(lines[1][0], lines[1][1]):
        b.append(i)

    for i in range(lines[2][0], lines[2][1]):
        c.append(i)


    # a, b, c 집합처리
    a, b, c = set(a), set(b), set(c)

    return len((a&b)|(b&c)|(c&a))