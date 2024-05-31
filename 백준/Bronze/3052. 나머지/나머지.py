import sys

answer = set()

for _ in range(10):
    n = int(sys.stdin.readline().rstrip())
    answer.add(n % 42)

print(len(answer))
