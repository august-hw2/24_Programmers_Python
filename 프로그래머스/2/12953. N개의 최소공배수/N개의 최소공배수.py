# 최소공배수 = a*b//최대공약수
import math
def solution(arr):
    ans = arr[0]

    for i in arr:
        ans = (i*ans)//math.gcd(i, ans)

    return ans