import sys

MAX = 1000001

primes = []
check = [True for _ in range(MAX+1)]
check[0] = False
check[1] = False

for i in range(2, int(MAX * 0.5) + 1):
    if check[i]:
        primes.append(i)
        for j in range(i * i, MAX+1, i):
            check[j] = False

N = int(input())

for _ in range(N):
    cnt = 0
    num = int(input())
    for p in primes:
        if p > num//2:
            break

        if check[num - p]:
            cnt +=1

    print(cnt)