import sys

input = sys.stdin.readline

A, N = map(int, input().split())
nums = list(map(int, input().split()))

dict = {0: 1}

answer = 0
sum = 0
for i in range(A):
    sum += nums[i]

    if sum - N in dict:
        answer += dict[sum - N]

    if sum in dict:
        dict[sum] += 1
    else:
        dict[sum] = 1

print(answer)