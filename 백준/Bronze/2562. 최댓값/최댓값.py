import sys

answer = [0, 0]

for i in range(9):
    tmp = int(sys.stdin.readline().rstrip())
    answer[0] = max(answer[0], tmp)
    if answer[0] == tmp:
        answer[1] = i

print(answer[0],answer[1]+1)