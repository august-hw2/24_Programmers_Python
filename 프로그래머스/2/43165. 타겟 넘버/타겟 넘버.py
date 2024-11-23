def solution(numbers, target):
    cnt = 0
    leaves = [0]

    for num in numbers:
        tmp = []

        # 자손 노드 넣기
        for leaf in leaves:
            tmp.append(leaf+num)
            tmp.append(leaf-num)

        leaves = tmp

    cnt = leaves.count(target)

    return cnt