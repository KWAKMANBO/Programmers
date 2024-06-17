import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

dq = deque()

for _ in range(n):
    inst = sys.stdin.readline().rstrip().split()

    # inst[0] == ""

    if inst[0] == "push_front":
        dq.appendleft(inst[1])
    elif inst[0] == "push_back":
        dq.append(inst[1])
    elif inst[0] == "pop_front":
        print(dq.popleft() if len(dq) > 0 else -1)
    elif inst[0] == "pop_back":
        print(dq.pop() if len(dq) > 0 else -1)
    elif inst[0] == "size":
        print(len(dq))
    elif inst[0] == "empty":
        print(0 if len(dq) > 0 else 1)
    elif inst[0] == "front":
        print(dq[0] if len(dq) > 0 else -1)
    else:
        print(dq[-1] if len(dq) > 0 else -1)
