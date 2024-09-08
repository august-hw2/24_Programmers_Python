def solution(num, total):
    tmp = []
    i = 1

    while True:

        for k in range(i, i+num):
            tmp.append(k)

        if total < sum(tmp):
            i -= 1
            tmp = []
        elif total > sum(tmp):
            i += 1
            tmp = []
        else:
            return tmp