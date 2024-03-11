def solution(array, n):
    answer = 0
    diff = []
    for i in array:
        if i > n:
            diff.append(i - n)
        else:
            diff.append(n - i)
    min_num = min(diff)
    if diff.count(min_num) > 1:
        return array[diff.index(min(diff))] if array[diff.index(min(diff))] < array[diff.index(min(diff), diff.index(min(diff))+1)] else array[diff.index(min(diff), diff.index(min(diff))+1)]     
  
    
    return array[diff.index(min(diff))]