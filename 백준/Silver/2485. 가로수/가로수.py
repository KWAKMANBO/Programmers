import sys


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


n = int(sys.stdin.readline())

num = int(sys.stdin.readline())

gaps = []
for i in range(n - 1):
    tmp = int(sys.stdin.readline())
    gaps.append(tmp - num)
    num = tmp

g = gaps[0]
for i in gaps[1:]:
    g = gcd(g, i)

answer = 0
for i in gaps:
    answer += i // g - 1

print(answer)
