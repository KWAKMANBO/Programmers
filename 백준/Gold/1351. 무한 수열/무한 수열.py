import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())

nums = {0: 1}


def dfs(i):
    if i not in nums:
        nums[i] = dfs(i // P) + dfs(i // Q)

    return nums[i]


print(dfs(N))
