import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break
    stack = []
    for w in s:
        if w == "(" or w == '[':
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)
        elif w == ']':
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(w)

    print('yes' if not stack else 'no')
