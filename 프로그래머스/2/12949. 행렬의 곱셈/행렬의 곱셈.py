def dot(A, B):
    return sum(a*b for a, b in zip(A, B))

def solution(arr1, arr2):
    answer = []

    for A in arr1:
        tmp = []
        for B in zip(*arr2):
            tmp.append(dot(A, B))
        answer.append(tmp)

    return answer