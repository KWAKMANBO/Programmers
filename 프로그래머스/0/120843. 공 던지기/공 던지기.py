def solution(numbers, k):
    cnt = 0
    idx = 0
    while cnt < k-1:
        if idx == len(numbers) -2 :
            idx = 0
        elif idx == len(numbers)-1:
            idx = 1
        else:
            idx +=2
        cnt +=1
        
    return numbers[idx]