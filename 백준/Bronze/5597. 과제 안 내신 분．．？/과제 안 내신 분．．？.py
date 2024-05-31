import sys

answer = [i for i in range(1, 31)]

for _ in range(28):
    answer.remove(int(sys.stdin.readline().rstrip()))

for i in answer:
    print(i)
