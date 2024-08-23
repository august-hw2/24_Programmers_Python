def solution(numbers):
    for k, v in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        numbers = numbers.replace(v, str(k))
        #enumerate(값, 인덱스 번호)

    return int(numbers)