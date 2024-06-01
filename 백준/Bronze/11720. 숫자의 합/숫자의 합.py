import sys

n = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()

answer = 0

for i in string:
    answer += int(i)

print(answer)
