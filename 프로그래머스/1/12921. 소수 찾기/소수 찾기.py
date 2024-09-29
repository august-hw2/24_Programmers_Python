import math

def is_prime(a):

    cnt = 0

    for m in range(2, int(math.sqrt(a)) + 1):
        if a%m == 0:
            return False
        
    return True

def solution(n):
    ans = 0

    for i in range(2, n+1):
        if is_prime(i):
            ans += 1

    return ans