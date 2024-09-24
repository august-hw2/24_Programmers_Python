def solution(left, right):
    l_r = [i for i in range(left, right+1)]
    ans = 0
    cnt = 0

    for i in l_r:
        for j in range(1, i+1):
            
            if i%j == 0:
                cnt += 1
                
        if cnt%2 == 0:
            ans += i
        else:
            ans -= i
            
        cnt = 0

    return ans