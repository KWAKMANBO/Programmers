nums = []

for _ in range(5):
    nums.append(int(input()))

nums.sort()
print(sum(nums) // len(nums))
print(nums[2])
