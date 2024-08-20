def solution(numbers):
    tmp = numbers[0]*numbers[1]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                tmp = max(tmp, numbers[i]*numbers[j])
    return tmp