n = int(input())

fibonacci = [0] * 91
fibonacci[1] = 1
fibonacci[2] = 1

if n > 2:
    for i in range(3, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

print(fibonacci[n])
