import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))
dict = {0: 1}
num_sum = 0
answer = 0

for i in range(N):
    num_sum += nums[i]

    if num_sum - K in dict:
        answer += dict[num_sum - K]

    if num_sum in dict:
        dict[num_sum] += 1
    else:
        dict[num_sum] = 1

print(answer)
