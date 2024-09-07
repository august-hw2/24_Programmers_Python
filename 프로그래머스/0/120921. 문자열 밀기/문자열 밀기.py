def solution(A, B):
    if A == B:
        return 0
    else:
        i = 0
        while i < len(A):
            B = B[1:] + B[0]
            i += 1
            if A == B :
                return i
    return -1