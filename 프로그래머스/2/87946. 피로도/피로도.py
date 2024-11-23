from itertools import permutations

def solution(k, dungeons):
    max = 0 # 갈 수 있는 던전의 최댓값
    permut = list(permutations(dungeons, len(dungeons)))  # 던전 탐험 순서의 순열

    for ds in permut:
        hp = k
        cnt = 0 # 던전 개수

        # 소모피로도 확인해서 가능한 던전만 돌기
        for minimum, waste in ds:
            if hp < minimum:
                break
            else:
                cnt += 1
                hp -= waste

        if max < cnt:
            max = cnt

    return max