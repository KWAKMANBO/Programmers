import sys

n = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(n):
    inst = list(sys.stdin.readline().rstrip().split())
    if inst[0] == "push":
        answer.append(inst[-1])
    elif inst[0] == "top":
        print(answer[-1] if len(answer) > 0 else -1)
    elif inst[0] == "size":
        print(len(answer))
    elif inst[0] == "empty":
        print(0 if len(answer) > 0 else 1)
    elif inst[0] == "pop":
        print(answer.pop() if len(answer) > 0 else -1)
