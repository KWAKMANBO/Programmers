import sys

n = int(sys.stdin.readline().rstrip())
lst = []
answer = 0
for i in range(1, n - 1):
    answer += i
    lst.append(answer)

print(sum(lst))
print(3)
