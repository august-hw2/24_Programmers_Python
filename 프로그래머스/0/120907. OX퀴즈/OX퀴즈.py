def solution(quiz):
    tmp = []
    ans = []

    for i in quiz:
        tmp = i.split(" ")
        if '+' in tmp: #덧셈
            ans.append("O") if int(tmp[0]) + int(tmp[2]) == int(tmp[4]) else ans.append("X")

        elif '-' in tmp: #뺄셈
            ans.append("O") if int(tmp[0]) - int(tmp[2]) == int(tmp[4]) else ans.append("X")

    return ans