import sys

k = int(sys.stdin.readline().rstrip())

lst = []
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)

print(sum(lst) if len(lst) > 0 else 0)
