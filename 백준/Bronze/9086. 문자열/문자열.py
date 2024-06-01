import sys
n =int(sys.stdin.readline().rstrip())


for _ in range(n):
    l = sys.stdin.readline().rstrip()
    print(l[0]+l[-1])
