# 종류 수 구하는 방법 = (아이템1 개수 + 1) * (아이템2 개수 + 1) - 1
def solution(clothes):

    #의상 종류 -> 딕셔너리 생성
    kind = dict()
    for i, j in clothes:
        kind[j] = kind.get(j, 0) + 1
        #get(값, 0) -> 이전에 값이 있다면 기존 값에 +1

    answer = 1

    for j in kind:
        answer *= (kind[j] + 1)

    return answer-1
