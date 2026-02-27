N = int(input())
answer = ""
while N > 0:
    r = str(N % 2)
    N //= 2

    answer += r

print(answer[::-1])