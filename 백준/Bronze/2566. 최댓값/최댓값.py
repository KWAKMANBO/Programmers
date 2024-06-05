import sys

matrix = []

for _ in range(9):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = -1
r = -1
c = -1
for i in range(len(matrix)):
    if max(matrix[i]) > answer:
        answer = max(matrix[i])
        r = i
        c = matrix[i].index(max(matrix[i]))

print(answer)
print(r+1,c+1)
