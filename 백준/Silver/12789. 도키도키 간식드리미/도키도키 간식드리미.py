import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lines = deque(list(map(int, input().split())))
stack = []

order = 1

while lines:
    current = lines.popleft()
    while stack and stack[-1] == order:
        stack.pop()
        order+=1
    if current == order:
        order+=1
    else:
        stack.append(current)

while stack:
    if stack[-1] == order:
        order+=1
        stack.pop()
    else:
        print("Sad")
        break
else:
    print("Nice")
