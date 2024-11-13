def solution(elements):
    ans = set()

    len_ = len(elements)
    elements = elements * 2

    for i in range(len_):
        for j in range(len_):
            ans.add(sum(elements[j:j+i+1]))

    return len(ans)
