import sys

n = int(sys.stdin.readline())
target_nums = set(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

answer = ""

for num in nums:
    if num in target_nums:
        print("1", end=" ")
    else:
        print("0", end=" ")

print(" ".join(answer))

