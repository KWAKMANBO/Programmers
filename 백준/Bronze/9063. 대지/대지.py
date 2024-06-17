import sys

n = int(sys.stdin.readline().rstrip())

if n < 2:
    print(0)
else:
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))

    xs = [i[0] for i in board]
    ys = [i[1] for i in board]

    print((max(xs) - min(xs)) * (max(ys) - min(ys)))
