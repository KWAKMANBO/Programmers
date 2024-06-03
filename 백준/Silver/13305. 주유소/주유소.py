import sys

n = int(sys.stdin.readline().rstrip())

distance = [int(i) for i in sys.stdin.readline().rstrip().split()]
fee = [int(i) for i in sys.stdin.readline().rstrip().split()]

f = fee[0]
answer = f * distance[0]
for i in range(1, len(distance)):
    if f > fee[i]:
        f = fee[i]
    answer += f * distance[i]

print(answer)
