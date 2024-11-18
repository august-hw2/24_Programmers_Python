from math import ceil
#올림 계산

def solution(progresses, speeds):
    answer = []

    #남은 작업량의 일수
    date = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]

    idx = 0 #현재 인덱스

    for i in range(len(date)):
        if date[idx] < date[i]: #현재 인덱스보다 다음 인덱스가 큰 경우
            answer.append(i-idx) #인덱스 차이만큼 answer리스트에 저장
            idx = i #현재 인덱스 갱신

    answer.append(len(date)-idx) #갱신된 인덱스부터 마지막 인덱스까지의 개수

    return answer