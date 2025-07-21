import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst1.extend(lst2)

lst1.sort()

print(*lst1)
