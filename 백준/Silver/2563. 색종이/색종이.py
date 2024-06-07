import sys

board = [[0] * 101 for i in range(101)]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

answer = 0
for i in board:
    answer += i.count(1)

print(answer)
