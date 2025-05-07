import sys

input = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

nums_dict = {}

for n in nums:
    if n in nums_dict:
        nums_dict[n] += 1
    else:
        nums_dict[n] = 1
max_nums = []
max_cnt = max(nums_dict.values())

for k in nums_dict:
    if nums_dict[k] == max_cnt:
        max_nums.append(k)
max_nums.sort()



print(round(sum(nums) / N))
print(nums[N // 2])
if len(max_nums) > 1:
    print(max_nums[1])
else:
    print(max_nums[0])
print(max(nums) - min(nums))
