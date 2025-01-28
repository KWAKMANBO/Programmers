import sys

lst = set()

n = int(sys.stdin.readline())

for _ in range(n):
    lst.add(sys.stdin.readline().strip())

lst = list(lst)
lst.sort(key=lambda x: (len(x), x))
for i in lst:
    print(i)
