# 1) 크기별로 개수 -> 딕셔너리 생성 후 정렬
# 2) 정렬된 귤(크기, 개수)로, 최솟값 찾기

from collections import Counter
# counter - 여러 형태의 데이터를 받아 중복된 데이터 개수 얻음 -> 딕셔너리로 얻음

def solution(k, tangerine):

    ans = 0
    cnt = Counter(tangerine)
    sort_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    # item값으로 정렬 -> reverse가 true이므로, 내림차순

    # 정렬된 귤(크기, 개수)로, 최솟값 찾기
    for i in sort_cnt:
        k -= i[1]
        ans += 1

        if k <= 0:
            break

    return ans