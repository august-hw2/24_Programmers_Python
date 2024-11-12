# 정렬 후, 가장 몸무게가 작은 사람과 큰 사람을 태운다. (2명만 가능하기 때문)
# 만약 limit를 넘는다면, 몸무게가 큰 사람만 태운다.

def solution(people, limit):
    ans = 0
    small, large = 0, len(people)-1

    # 정렬하기
    people.sort()

    while small <= large:
        if people[small] + people[large] <= limit:
            small += 1
            large -= 1
        else:
            large -= 1

        ans += 1

    return ans