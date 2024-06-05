import sys

matrix = []
answer = ""
length = 0
for i in range(5):
    matrix.append(sys.stdin.readline().rstrip())
    length = max(length, len(matrix[i]))

for c in range(length):
    for r in range(5):
        try:
            answer += matrix[r][c]
        except:
            continue


print(answer)
