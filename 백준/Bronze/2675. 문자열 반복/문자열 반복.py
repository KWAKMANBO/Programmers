import sys

n = int(sys.stdin.readline().rstrip())



for _ in range(n):
    r, s = sys.stdin.readline().rstrip().split()
    r = int(r)
    tmp = ""
    for i in s:
        tmp += i*r
    print(tmp)