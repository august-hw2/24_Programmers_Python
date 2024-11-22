def solution(s):
    answer = []
    tmp = [] # 정렬 용도 리스트

    # 값 별로 나누기
    for i in s.split("},"):
        tmp.append((i.replace("{","").replace("}","")).split(","))

    # 정답 찾기 -> 순서도 확인해서
    tmp.sort(key=len)

    for i in tmp:
        for j in i:
            if j not in answer:
                answer.append(j)

    return list(map(int, answer))