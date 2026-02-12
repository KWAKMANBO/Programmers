N = int(input())


felindromes = []

for _ in range(N):
    tmp = input()
    if tmp == tmp[::-1]:
        felindromes.append(tmp)
length = len(felindromes)

print(length * (length - 1))
