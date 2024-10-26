def solution(s, skip, index):
    ans = ''

    alphabet = sorted(list(set([chr(i) for i in range(97, 123)]) - set(skip)))

    for i in s:
        ans += alphabet[(alphabet.index(i) + index)%len(alphabet)]

    return ans