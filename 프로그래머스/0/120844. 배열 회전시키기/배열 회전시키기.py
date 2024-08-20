def solution(numbers, direction):
    if direction == "right":
        tmp = numbers.pop()
        numbers.insert(0, tmp)
    else:
        tmp = numbers[0]
        del numbers[0]
        numbers.append(tmp)
    return numbers