cnt = 0

# DFS
def solution(numbers, target):
    global cnt
    def dfs(depth, s, target):
        global cnt
        if depth == len(numbers) and s == target:
            cnt += 1

        if depth == len(numbers):
            return

        dfs(depth + 1, s + numbers[depth], target)
        dfs(depth + 1, s - numbers[depth], target)

    dfs(0, 0, target)


    return cnt