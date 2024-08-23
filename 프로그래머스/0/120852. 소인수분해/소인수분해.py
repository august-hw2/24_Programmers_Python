def solution(n):
    res = []

    for i in range(2, n+1):
        if n%i == 0:
            res.append(i)

    for i in res:
        cnt = 0
        for j in range(1, i+1):
            if i%j == 0:
                cnt += 1

        if cnt >= 3: #소인수는 약수로 자기자신과 1만 있기 때문에, 3 이상의 약수를 가진다면 소인수에 해당하지 않음
            res[res.index(i)] = 0

    return [i for i in res if i!=0]