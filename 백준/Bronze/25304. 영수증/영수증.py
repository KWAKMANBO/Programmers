import sys

money = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    money -= a * b

if money == 0:
    print("Yes")
else:
    print("No")
