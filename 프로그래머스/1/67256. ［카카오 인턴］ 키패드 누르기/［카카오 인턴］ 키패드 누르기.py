def solution(numbers, hand):

    # 거리 동일 시, 미리 구분한 변수로 값 더해줌
    if hand == "right":
        person = 'R'
    elif hand == "left":
        person = 'L'

    # 키패드 위치 -> 좌표화
    keypad = {1:[0, 0], 2:[0, 1], 3:[0, 2]
            , 4:[1, 0], 5:[1, 1], 6:[1, 2]
            , 7:[2, 0], 8:[2, 1], 9:[2, 2]
            ,'*':[3, 0], 0:[3, 1], '#':[3, 2]}

    # 오른손, 왼손 시작 위치
    right_l = keypad['*']
    left_l = keypad['#']

    ans = ''

    # numbers 요소 순회 -> 오른쪽, 왼쪽 문자열 더하기
    for i in numbers:
        now = keypad[i]

        if i in [1, 4, 7]: #왼손
            ans += 'L'
            left_l = now
        elif i in [3, 6, 9]: #오른손
            ans += 'R'
            right_l = now
        else: # 2, 5, 8, 0 누르는 경우
            right_d = 0 # 거리 변수
            left_d = 0

            for l, r, n in zip(left_l,right_l, now):
                left_d += abs(l-n)
                right_d += abs(r-n)

            # 거리 비교
            if left_d < right_d: #왼손이 가까운 경우
                ans += 'L'
                left_l = now
            elif left_d > right_d: #오른손이 가까운 경우
                ans += 'R'
                right_l = now
            else: #동일한 경우
                if hand == "left": # 왼손잡이인 경우
                    ans += 'L'
                    left_l = now
                else:
                    ans += 'R' # 오른손잡이인 경우
                    right_l = now

    return ans