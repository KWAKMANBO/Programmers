N, M, K = map(int, input().split())

nums = [int(i) for i in input().split()]


nums.sort(reverse= True)
answer =0
for i in range(1,M+1):
    if i % K == 0:
        answer += nums[1]
    else:
        answer += nums[0]

print(answer)