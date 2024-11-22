from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)

    while dq:
        t = dq.popleft()
        sec = 0

        for j in dq:
            sec += 1
            if j < t:
                break
                
        answer.append(sec)

    return answer