import sys

line = sys.stdin.readline().rstrip()

if line == line[::-1]:
    print(1)
else:
    print(0)

