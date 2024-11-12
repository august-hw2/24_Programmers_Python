def solution(n, words):
    ans = [0, 0]
    stack = []
    person = [0 for i in range(n)]

    for i in range(len(words)):
        person[i%n] += 1
        ans[0], ans[1] = i%n+1, person[i%n]

        # 이전 단어의 마지막 알파벳 == 현재 단어의 첫번째 알파벳 확인
        if i > 0:
            prev, now = stack[-1], words[i]
            if prev[-1] != now[0]:
                return ans

        # 겹치는 단어 확인
        if words[i] not in stack:
            stack.append(words[i])
        else:
            return ans

    return [0, 0]