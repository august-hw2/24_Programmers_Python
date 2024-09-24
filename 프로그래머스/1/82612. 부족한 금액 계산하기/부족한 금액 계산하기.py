def solution(price, money, count):
    s = 0

    for i in range(1, count+1):
        s += price*i
        
    return s - money if s>money else 0