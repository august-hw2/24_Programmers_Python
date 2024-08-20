def solution(sides):
    sides.sort()
    return 1 if sum(sides[0:2]) > sides[2] else 2