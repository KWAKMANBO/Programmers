import sys

lines = list(map(int, sys.stdin.readline().rstrip().split()))

lines.sort()

if lines[2] < lines[0] + lines[1]:
    print(sum(lines))
else:
    lines[2] = lines[1] + lines[0] - 1
    print(sum(lines))
