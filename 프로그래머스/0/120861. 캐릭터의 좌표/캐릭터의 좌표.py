def solution(keyinput, board):
    res = [0, 0]

    for i in keyinput:

        if "left" == i and res[0]-1 >= -(board[0]//2):
            res[0] -= 1
        elif "right" == i and res[0]+1 <= (board[0]//2):
            res[0] += 1
        elif "up" == i and res[1]+1 <= (board[1]//2):
            res[1] += 1
        elif "down" == i and res[1]-1 >= -(board[1]//2):
            res[1] -= 1
            
    return res