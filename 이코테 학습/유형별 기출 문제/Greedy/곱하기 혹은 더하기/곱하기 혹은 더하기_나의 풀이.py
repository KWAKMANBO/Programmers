import sys

nums = input().strip()
answer = 0
for ch in nums:
    n = int(ch)
    answer = max(answer + n, answer * n)

print(answer)
