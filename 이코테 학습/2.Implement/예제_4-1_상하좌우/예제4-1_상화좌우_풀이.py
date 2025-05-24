import sys

input = sys.stdin.readline

N = int(input())

dir = {'R': (0, 1), 'L': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

inst = input().split()
pos = (1, 1)

for i in inst:
    dx, dy = dir[i]
    nx, ny = pos[0] + dx, pos[1] + dy

    if 0 < nx <= N and 0 < ny <= N:
        pos = (nx, ny)

print(pos[0], pos[1])
