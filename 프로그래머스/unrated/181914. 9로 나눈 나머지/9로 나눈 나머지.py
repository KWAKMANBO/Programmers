def solution(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
        
    
    return sum % 9