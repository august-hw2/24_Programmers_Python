def solution(X, Y):
    ans = []
    # 겹치는 숫자들 answer에 모음
    # 큰 수부터 처리함으로써 나중에 sort 안해도 되게끔 유도
    for i in range(9, -1, -1):
        ans.append(str(i) * min(X.count(str(i)), Y.count(str(i))))

    # 문자열들을 다 합치고 연산
    string = ''.join(ans)
    if not string:
        return '-1'
    # 다 0이면 '000'으로 출력되지 않고, 0으로 처리하도록 조건 분기
    elif len(string) == string.count('0'):
        return '0'
    else:
        return string


""" 테스트케이스 11 - 15 시간 초과

    ans = ''
    sort_x, sort_y = sorted(X), sorted(Y)
    
    # dictinary -> X, Y 속 숫자들의 횟수를 저장
    dict_x , dict_y = {}, {}
    for i in sort_x:
        dict_x[i] = sort_x.count(i)
    for j in sort_y:
        dict_y[j] = sort_y.count(j)

    # 같은 key에서 value값이 더 크거나 같은 숫자만 ans에 추가
    for key_x, value_x in dict_x.items():
        for key_y, value_y in dict_y.items():
            tmp = ''
            # key가 동일한 경우 -> value값 비교해 최소값에 해당하는 key값 저장
            if key_x == key_y:
                tmp = key_x*value_x if value_x <= value_y else key_y*value_y

            if tmp not in ans:
                ans += tmp
    ans = ''.join(sorted(ans, reverse=1))

    if not ans:
        return '-1'
    elif len(ans) == ans.count('0'):
        return '0'
    else:
        return ans

    #return str(int(''.join(sorted(ans, reverse=1)))) if ans != '' else '-1'

"""