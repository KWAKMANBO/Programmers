array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

lst = [0] * (max(array) + 1)

for n in array:
    lst[n] += 1

for n in range(len(lst)):
    for i in range(lst[n]):
        print(n, end=" ")
