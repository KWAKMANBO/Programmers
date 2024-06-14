import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    distance = abs((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if distance == r1 + r2:
        print(1)
    elif distance > r1 + r2:
        print(0)
    elif distance == 0 and r1 == r2:
        print(-1)
    elif distance == max(r2, r1) - min(r2, r1):
        print(1)
    elif distance < max(r2, r1) - min(r2, r1):
        print(0)
    elif distance > max(r2, r1) - min(r2, r1):
        print(2)
