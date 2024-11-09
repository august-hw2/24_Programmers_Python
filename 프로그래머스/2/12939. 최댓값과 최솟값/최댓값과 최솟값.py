def solution(s):

    tmp = list(map(int, s.split(' ')))

    return str(min(tmp)) + " " + str(max(tmp))