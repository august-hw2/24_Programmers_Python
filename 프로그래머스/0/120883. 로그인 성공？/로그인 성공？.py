def solution(id_pw, db):
    
    cnt = 0

    for i in db:
        if id_pw == i:
            return "login"

        if id_pw[0] == i[0] and id_pw[1] != i[1]:
            cnt += 1

    if cnt:
        return "wrong pw"
    else:
        return "fail"