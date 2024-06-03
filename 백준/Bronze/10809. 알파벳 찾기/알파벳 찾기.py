import sys

string = sys.stdin.readline().rstrip()

answer = []

for i in range(97,123):
    answer.append(string.find(chr(i)))

print(*answer)