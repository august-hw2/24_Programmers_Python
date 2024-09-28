def solution(answers):
    x = [1, 2, 3, 4, 5]
    y = [2, 1, 2, 3, 2, 4, 2, 5]
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0] #맞은 점수 저장하는 리스트
    ans = []

    for i in range(len(answers)):
        if answers[i] == x[i%5]:
            score[0] += 1
        if answers[i] == y[i%8]:
            score[1] += 1
        if answers[i] == z[i%10]:
            score[2] += 1

    #점수 순으로 정렬
    for idx, num in enumerate(score) :
        if num == max(score) :
            ans.append(idx+1)
            
    return ans