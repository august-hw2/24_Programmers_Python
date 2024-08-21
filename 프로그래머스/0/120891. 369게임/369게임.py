def solution(order):
    tmp = str(order)

    return  tmp.count('3') + tmp.count('6') + tmp.count('9')