import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().strip()
    if len(s)%2 == 1:
        print("NO")
        continue
    stack =[]
    for i in s:
        stack.append(i)
        if len(stack)>1 and stack[-1] == ")" and stack[-2] == "(" :
            stack.pop()
            stack.pop()
    #print(stack)
    if not stack:
        print("YES")
    else:
        print("NO")
