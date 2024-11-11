def solution(n):
    answer = 0
    fibon = [0, 1]

    for i in range(2, n+1):
        fibon.append(fibon[i-2]+fibon[i-1])

    return fibon[-1]%1234567