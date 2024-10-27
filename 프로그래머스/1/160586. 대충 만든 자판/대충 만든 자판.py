def solution(keymap, targets):
    ans = []
    dict_keymap = {}

    # keymap에 있는 문자열 속 문자들 모두 저장 (단, 중복은 최소값만 저장)
    for i in range(len(keymap)):
        for j in range(len(keymap[i])): # keymap의 문자열들의 길이가 다 다르기 때문
            tmp = keymap[i][j]
            if tmp not in dict_keymap:
                dict_keymap[tmp] = j+1 #인덱스 + 1
            else: # 중복인 경우, 저장된 값과 새로운 값 비교 후 최소값만 저장
                dict_keymap[tmp] = min(dict_keymap[tmp], j+1)

    # 최소값만 저장된 dict_keymap 이용 -> targets 리스트 내 문자열 횟수 더하기
    for x in targets:
        s = 0
        char = list(x)
        for y in char:
            if y in dict_keymap:
                s += dict_keymap[y]
            else:
                s = -1
                break #입력할 수 없는 문자열 포함 시, 반복문 멈춤
        ans.append(s)

    return ans