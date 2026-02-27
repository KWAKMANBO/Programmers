N = int(input())

nums = list(map(int, input().split()))

m = nums[0]
is_asc = True

for i in range(1, len(nums)):
    if nums[i] > m:
        m = nums[i]
    else:
        is_asc=False
        break

print(int(is_asc))
