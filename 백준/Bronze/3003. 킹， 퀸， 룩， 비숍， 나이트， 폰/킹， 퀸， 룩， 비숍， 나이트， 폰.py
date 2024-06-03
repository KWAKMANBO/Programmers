import sys

lst = [1, 1, 2, 2, 2, 8]

chess = [int(i) for i in sys.stdin.readline().rstrip().split()]

answer = []

for i in range(len(chess)):
    answer.append(lst[i] - chess[i])

print(* answer)