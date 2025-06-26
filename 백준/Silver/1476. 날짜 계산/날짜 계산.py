import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())
E -= 1
S -= 1
M -= 1

e, s, m = -1, -1, -1
answer = 0

while True:
    e += 1
    s += 1
    m += 1
    answer += 1
    if (e % 15) == E and (s % 28) == S and (m % 19) == M:
        break

print(answer )
