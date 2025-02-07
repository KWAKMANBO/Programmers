def solution(s):
    stack = [s[0]]

    for i in s[1:]:
        if  i not in stack or i != stack[-1]:
            stack.append(i)
        elif i == stack[-1] :
            stack.pop()

    return 1 if not stack else 0