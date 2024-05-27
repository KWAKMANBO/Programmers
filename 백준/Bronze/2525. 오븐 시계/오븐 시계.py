import sys

h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

h = (h + (m + t) // 60) % 24
m = (m + t) % 60
print(h, m)
