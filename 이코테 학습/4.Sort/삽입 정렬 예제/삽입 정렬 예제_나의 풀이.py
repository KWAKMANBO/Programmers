array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        # 크다면 j보당 뒤에
        if array[j-1] > array[j]:
            array[j-1],array[j] = array[j],array[j-1]
print(array)