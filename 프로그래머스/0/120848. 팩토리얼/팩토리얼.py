def solution(n):
    
    i = 1
    cnt = 1 #+1씩 곱하는 수
    
    while True:
        
        i *= cnt
        
        if i > n:
            return cnt-1
    
        cnt += 1