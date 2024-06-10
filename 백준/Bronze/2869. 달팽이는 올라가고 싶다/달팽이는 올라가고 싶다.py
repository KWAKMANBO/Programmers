import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())
h = 0
days = 0
if V < A:
    print(1)
else:
    if (V - A) % (A - B) != 0:
        print((V - A) // (A - B) + 1 + 1)
    else:
        print((V - A) // (A - B) + 1)
