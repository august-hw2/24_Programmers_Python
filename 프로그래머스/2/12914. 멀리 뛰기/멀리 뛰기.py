def solution(n):
    fibon = [0] * (n+1)

    fibon[0], fibon[1] = 1, 2

    for i in range(2, n):
        fibon[i] = fibon[i-2] + fibon[i-1]

    return fibon[n-1]%1234567