import sys

N, B = map(int, sys.stdin.readline().rstrip().split())

answer = ""

while N > 0:
    tmp = N % B
    N //= B
    if tmp >= 10:
        answer += chr(tmp + 55)
    else:
        answer += str(tmp)

print(answer[::-1])
