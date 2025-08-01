array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(pivot, start, end):
    while start <= end:
        if array[start] > array[pivot] and array[end] < array[pivot]:
            array[start], array[end] = array[end], array[start]
        elif array[start] < array[pivot]:
            start += 1
        elif array[end] > array[pivot]:
            end -= 1
    if array[start] < array[end]:
        array[pivot], array[start] = array[start], array[pivot]
    else:
        array[pivot], array[end] = array[end], array[pivot]
    quick_sort(0,1,start)
    quick_sort(end,end+1, len(array)-1)

print(array)
quick_sort(0, 1, len(array) - 1)
print(array)
