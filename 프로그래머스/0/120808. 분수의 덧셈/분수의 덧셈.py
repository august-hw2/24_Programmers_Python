import math

def solution(numer1, denom1, numer2, denom2):
    
    gcd = denom1 * denom2 // math.gcd(denom1, denom2) #최소공배수

    tmp1 = ((gcd // denom1) * numer1) + ((gcd // denom2) * numer2)
    tmp2 = gcd

    #기약분수로 만들기 위해, 분자와 분모의 최대공약수로 나누어 줌
    return [tmp1 // math.gcd(tmp1, tmp2), tmp2 // math.gcd(tmp1, tmp2)]