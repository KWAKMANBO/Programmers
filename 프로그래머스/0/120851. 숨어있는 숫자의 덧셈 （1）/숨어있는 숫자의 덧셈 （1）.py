def solution(my_string):
    answer = 0
    sum = 0
    for i in my_string:
        if ord(i) > 47 and ord(i) < 58:
           sum += (ord(i) - 48)
    
    return sum