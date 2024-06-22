N, M = map(int, input().split())

lst = [int(i) for i in input().split()]

answer = 0
for i in range(len(lst) - 2):
    for j in range(i + 1, len(lst) - 1):
        for k in range(j + 1, len(lst)):
            if answer < lst[i] + lst[j] + lst[k] <= M:
                answer = lst[i] + lst[j] + lst[k]

print(answer)
