def solution(array, n):
    array = sorted(array)
    tmp = [abs(n-i) for i in array]

    return array[tmp.index(min(tmp))]