from collections import deque

def solution(s):

    ans = 0
    dq = deque(s)

    len_s = len(s)

    for i in range(len_s):
        stack = []

        for j in range(len_s):

            stack.append(dq[j])

            if len(stack) > 1:
                if stack[-2] == '(' and stack[-1] == ')':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '[' and stack[-1] == ']':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '{' and stack[-1] == '}':
                    stack.pop()
                    stack.pop()


        if len(stack) == 0:
            ans += 1

        dq.rotate(1)


    return ans