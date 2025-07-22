import sys

input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))
answer = 0


def solve(depth, lst):
    global answer

    if depth == N:
        # print(lst, sum(lst))
        if sum(lst) == S and len(lst) > 0:
            answer += 1
        return

    lst.append(nums[depth])
    solve(depth + 1, lst)
    lst.pop()
    solve(depth + 1, lst)


solve(0, [])
print(answer)
