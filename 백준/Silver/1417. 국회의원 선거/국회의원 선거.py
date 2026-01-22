candidates = []

n = int(input())
if n == 1:
    print(0)
    exit()
for i in range(n):
    candidates.append(int(input()))

ds = candidates[0]
candidates_except_ds = candidates[1:]
candidates_except_ds.sort(reverse=True)

answer = 0
while True:
    if ds > candidates_except_ds[0]:
        break

    candidates_except_ds[0] -= 1
    ds +=1
    answer +=1
    candidates_except_ds.sort(reverse=True)

print(answer)