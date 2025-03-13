import sys


def get_primes(n):
    end = int(n ** 0.5) + 1
    arr = [i for i in range(n + 1)]
    for i in range(2, end):
        if arr[i] == 0:
            continue
        for j in range(i * i, n + 1, i):
            arr[j] = 0
    arr[0] = 0
    arr[1] = 0
    return arr, [i for i in arr[2:] if i]


input = sys.stdin.readline

n = int(input())
arr, primes = get_primes(1000000)

for _ in range(n):
    num = int(input())
    cnt = 0
    for p in primes:
        if p > num // 2: break
        if arr[num - p]:
            cnt += 1
    print(cnt)
