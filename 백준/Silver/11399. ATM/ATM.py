n = int(input())

atm = [int(i) for i in input().split()]

atm.sort()

for i in range(1, n):
    atm[i] = sum(atm[i - 1:i + 1])

print(sum(atm))
