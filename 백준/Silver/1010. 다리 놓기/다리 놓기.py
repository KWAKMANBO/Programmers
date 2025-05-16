import math
import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    w, e = map(int, input().split())
    print(math.factorial(e)// (math.factorial(w)*math.factorial(e-w)))

