N = int(input())

for _ in range(N):
    h, w, n = map(int, input().split())

    answer = []

    if n == 1:
        print("101")
    else:
        # 층
        answer.append(str(n % h) if n % h else str(h))
        # 호
        answer.append(str(n // h + 1).zfill(2) if n % h != 0 else str(n // h).zfill(2))
        print(answer[0] + answer[1])
