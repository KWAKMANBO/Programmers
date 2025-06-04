import sys

input = sys.stdin.readline

s = input().strip()

lst = []
for i in range(len(s)):
    lst.append(s[i:])

lst.sort()

for l in lst:
    print(l)
