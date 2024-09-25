def solution(sizes):
    tmp_min = []
    tmp_max = []

    for i in sizes:
        i.sort()
        tmp_min.append(min(i))
        tmp_max.append(max(i))

    return max(tmp_min) * max(tmp_max)