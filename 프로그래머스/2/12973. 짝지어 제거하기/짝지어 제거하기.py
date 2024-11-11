def solution(s):
    answer = -1
    stack = []

    for i in range(len(list(s))):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                del stack[-1]
            else:
                stack.append(s[i])


    return 0 if len(stack) else 1