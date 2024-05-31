import sys

n = int(input())

rope = []

answer = 0
length = n
for _ in range(n):
    rope.append(int(sys.stdin.readline().rstrip()))

rope.sort()

for i in rope:
    if i * length > answer:
        answer = i * length

    length -= 1

print(answer)
