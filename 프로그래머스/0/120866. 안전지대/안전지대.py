def solution(board):
    ans = 0
    n = len(board)

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    #폭탄의 위치 저장할 리스트
    boom = []

    #폭탄 위치 찾아서 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                boom.append((i, j))

    #폭탄 위치 리스트로부터 배열의 범위를 벗어나지 않는 곳에만 0에서 1로 바꿔줌
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1

    for i in board:
        ans += i.count(0)
    
    return ans