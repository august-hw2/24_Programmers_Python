def solution(ingredient):
    # stack 개념 이용
    ing = []
    cnt = 0

    for i in ingredient:
        ing.append(i)
        if ing[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del ing[-4:]

    return cnt

""" 테스트케이스 3-12, 18 실패

    str_in = "".join(str(i) for i in ingredient)
    cnt = 0 # 완성시킬 수 있는 버거 개수


    # 1231 문자열이 있는 경우에만
    while "1231" in str_in:
        cnt += 1
        str_in = str_in.replace("1231", "")

    return cnt

# 빵 = 1, 야채 = 2, 고기 = 3
# 햄버거 = 빵 + 야채 + 고기 + 빵 = 1231
"""