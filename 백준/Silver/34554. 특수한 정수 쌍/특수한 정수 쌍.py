import sys

input = sys.stdin.readline


def is_prime(N):
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True


# A * B 정확히 2개 -> 소수
# A는 무조건 1

T = int(input())

for _ in range(T):
    N = int(input())
    B = 1 + N
    answer = []
    cnt = 0

    if is_prime(B):
        answer.append((1, B))
        cnt += 1

    print(cnt)
    for a in answer:
        print(a[0], a[1])
