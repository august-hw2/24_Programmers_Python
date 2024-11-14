from collections import Counter

def solution(want, number, discount):
    answer = 0

    # zip 함수
    all_want = {}
    for w, n in zip(want, number):
        all_want[w] = n


    for i in range(len(discount)-9):
        tmp = Counter(discount[i:i+10])
        if tmp == all_want:
            answer += 1

    return answer