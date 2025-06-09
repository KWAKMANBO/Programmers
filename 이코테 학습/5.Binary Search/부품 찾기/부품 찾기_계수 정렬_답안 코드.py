# Input
# 5
# 8 3 7 9 2
# 3
# 5 7 9

n = int(input())
array = [0] * 1000001

for i in map(int, input().split()):
    array[i] += 1

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if array[t]:
        print("yes", end=" ")
    else:
        print("no", end=" ")
