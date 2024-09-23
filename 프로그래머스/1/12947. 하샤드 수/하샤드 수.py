def solution(x):
    return False if x%sum(int(i) for i in str(x)) else True