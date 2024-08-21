def solution(order):
    tmp = list(map(int, str(order)))
    cnt = 0
    for i in tmp:
        if i == 3 or i == 6 or i == 9:
            cnt += 1
    return cnt