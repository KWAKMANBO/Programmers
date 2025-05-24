N, M, K = map(int, input().split())

nums = [int(i) for i in input().split()]

nums.sort(reverse=True)
answer = (M // (K + 1)) * (nums[0] * K + nums[1]) + (M % (K + 1)) * nums[0]
print(answer)
