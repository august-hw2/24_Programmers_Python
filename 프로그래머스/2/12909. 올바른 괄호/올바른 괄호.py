def solution(s):

    stack = []

    for char in s:
        #스택에 아무것도 없는데, 닫힌 괄호 들어올 때
        if len(stack) == 0 and char == ')':
            return False

        if char == ')' and stack[-1] == '(':
            stack.pop()

        if char == '(':
            stack.append(char)

    return False if len(stack) else True