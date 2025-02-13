import sys

n = int(sys.stdin.readline().strip())


def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a,b))
