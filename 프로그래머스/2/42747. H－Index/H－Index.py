# idx랑 citations 요소가 동일할 때까지의 개수 합

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] >= i+1:
            h_idx = i+1
            answer += 1

    return answer