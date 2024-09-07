def solution(polynomial):
    a = 0 #x 앞 숫자
    b = 0 #상수

    tmp = polynomial.split(" ")

    for i in tmp:
        if 'x' in i: #x 수 덧셈
            x_tmp = "".join(i.split("x"))
            if x_tmp == "":
                a += 1
            else:
                a += int(x_tmp)
        elif i.isdigit():
            b += int(i)
        elif i == "+":
            pass
    
    if a != 0 and b != 0:
        return 'x + ' + str(b) if a == 1 else str(a)+'x + '+str(b)
    elif a != 0:
        return 'x' if a == 1 else str(a)+'x'
    elif a == 0:
        return str(b)