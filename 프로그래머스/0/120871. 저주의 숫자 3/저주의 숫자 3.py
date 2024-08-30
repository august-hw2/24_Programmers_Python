def solution(n):
    arr = []

    for i in range(300):
        if i%3 == 0 or str(i).find('3') != -1:
            pass
        else:
            arr.append(i)
            
    return arr[n-1]