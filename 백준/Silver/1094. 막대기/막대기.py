import sys
from collections import deque

input = sys.stdin.readline

sticks = [64]

X = int(input())

while True:
    sum_sticks = sum(sticks)
    if sum_sticks > X:
        half = sticks[0] // 2
        if sum_sticks - half > X:
            sticks[0] = half
        else:
            sticks[0] = half
            sticks.append(half)
        sticks.sort()

    if sum(sticks) < X :
        break
    elif sum(sticks) == X:
        answer = [s for s in  sticks if s != 0]
        print(len(answer))
        break
