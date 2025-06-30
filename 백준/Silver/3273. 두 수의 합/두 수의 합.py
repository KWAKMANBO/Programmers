import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()
X = int(input())

start = 0
end = N - 1
answer = 0
while start < end:
    l = nums[start]
    r = nums[end]

    if l + r > X:
        end -= 1
    elif l + r < X:
        start += 1
    else:
        answer += 1
        start += 1
print(answer)