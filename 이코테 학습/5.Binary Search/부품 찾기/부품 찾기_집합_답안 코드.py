# Input
# 5
# 8 3 7 9 2
# 3
# 5 7 9

n = int(input())
nums = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in nums:
        print("yes", end = " ")
    else:
        print("no", end = " ")