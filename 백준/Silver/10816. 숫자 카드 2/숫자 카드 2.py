import sys

n = int(sys.stdin.readline())

cards = {}

for i in list(map(int, sys.stdin.readline().split())):
    if cards.get(i):
        cards[i] += 1
    else:
        cards[i] = 1

m = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    print(cards[i] if cards.get(i) else 0, end= " ")
