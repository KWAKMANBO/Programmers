import sys

n = int(sys.stdin.readline().rstrip())

score = [int(i) for i in sys.stdin.readline().rstrip().split()]

m = max(score)

for i in range(n):
    score[i] = score[i] / m * 100

print(sum(score)/len(score))
