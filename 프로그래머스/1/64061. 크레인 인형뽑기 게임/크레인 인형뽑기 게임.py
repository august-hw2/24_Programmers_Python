def solution(board, moves):
    ans = 0 # 사라진 인형의 개수
    stack = [] # 뽑은 인형 저장 리스트

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: # 인형이 0이 아닐 때만 stack에 저장
                stack.append(board[j][i-1])
                board[j][i - 1] = 0

                if len(stack) > 1: #뽑은 인형들 중 겹치면, 삭제
                    if stack[-1] == stack[-2]:
                        stack.pop(-1) # 동일한 경우, 숫자 2개 모두 삭제
                        stack.pop(-1)
                        ans += 2
                break #맨 위 인형 뽑으면 moves의 다음 요소로 넘어감
    return ans