import sys


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


N = int(sys.stdin.readline())

for _ in range(N):
    n = int(sys.stdin.readline())

    while True:
        if n == 0 or n == 1:
            print(2)
            break
        else:
            if isPrime(n):
                print(n)
                break
        n += 1
