N = input()
intN = int(N)

minimum = max(1, intN - 9 * len(N))

for s in range(minimum, intN + 1):
    tmp = s
    sums = sum(map(int, list(str(s))))
    tmp += sums

    if tmp == intN:
        print(s)
        break
    elif s == intN:
        print(0)
