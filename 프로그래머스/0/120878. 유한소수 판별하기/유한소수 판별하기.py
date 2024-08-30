import math

def solution(a, b):
    
    #분모 / a와 b의 최대공약수
    b /= math.gcd(a, b)

    #분모를 2와 5로 나눈 값이 0일 때만 반복
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
        
    return 1 if b==1 else 2