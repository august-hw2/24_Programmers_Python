def solution(number, limit, power):
    
    #숫자에 따른 약수 개수 구하기
    ans = []

    for i in range(2, number+1):
        cnt = 0
        for j in range(1, int(i ** (1 / 2)) + 1):  
        # ★포인트1. 제곱근만큼만 반복
            if i % j == 0:
                if j == i // j:  
                # 제곱근일 경우 -> 1개만 카운트하기
                    cnt += 1
                else:
                    cnt += 2
        if cnt > limit:
            ans.append(power)
        else:
            ans.append(cnt)

    return sum(ans)+1