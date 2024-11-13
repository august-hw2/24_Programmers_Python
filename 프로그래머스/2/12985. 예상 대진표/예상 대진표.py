def solution(n,a,b):
    ans = 0
    
    while True:
        a, b = (a//2)+(a%2), (b//2)+(b%2)
        ans += 1

        if a == b:
            return ans