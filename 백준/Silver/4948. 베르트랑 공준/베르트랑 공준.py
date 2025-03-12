import sys

input = sys.stdin.readline
nums = []

while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)
n = max(nums) * 2 + 1
arr = [i for i in range(n)]
arr[0] = 0
arr[1] = 0
end = int(n ** 0.5)
for i in range(2, end):
    if arr[i] == 0:
        continue
    for j in range(i * i, n, i):
        arr[j] = 0

for i in nums:
    cnt = 0
    for j in range(i + 1, i * 2 + 1):
        if arr[j] != 0:
            cnt += 1
    print(cnt)