array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(start, end):
    if start >= end:
        return

    # pivot은 start로부터 계산하기
    pivot = start
    left = start + 1
    right = end

    # left와 right가 교차할때까지 반복
    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while right > pivot and array[right] > array[pivot]:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

quick_sort(0,len(array)-1)
print(array)
