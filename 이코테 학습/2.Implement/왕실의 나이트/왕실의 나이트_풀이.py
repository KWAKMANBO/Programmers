import sys

input = sys.stdin.readline

coor = input()

alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'h': 6, 'i': 7}

pos = (alpha[coor[0]], int(coor[1]) - 1)

dir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

answer = 0

for d in dir:
    nx = pos[0] + d[0]
    ny = pos[1] + d[1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1

print(answer)
