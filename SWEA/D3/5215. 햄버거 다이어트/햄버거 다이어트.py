t = int(input())


def dfs(index, currentTaste, currentCal):
    global maxTaste

    if currentCal > l:
        return

    if maxTaste < currentTaste:
        maxTaste = currentTaste

    if index == n:
        return

    taste, kcal = data[index]
    dfs(index + 1, currentTaste + taste, currentCal + kcal)
    dfs(index + 1, currentTaste, currentCal)


for test_case in range(1, t + 1):
    n, l = map(int, input().split())

    maxTaste = 0

    data = [list(map(int, input().split())) for _ in range(n)]

    dfs(0, 0, 0)

    print(f"#{test_case} {maxTaste}")