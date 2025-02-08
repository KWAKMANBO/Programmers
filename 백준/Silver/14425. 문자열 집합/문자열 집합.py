import sys

N, M = map(int, sys.stdin.readline().split())

inspect_set = set()

for i in range(N):
    inspect_set.add(sys.stdin.readline().strip())
inspect_word_list = []
for i in range(M):
    inspect_word_list.append(sys.stdin.readline().strip())

answer = 0
for i in inspect_word_list:
    if i in inspect_set:
        answer += 1

print(answer)
