def solution(my_string, indices):
    answer = list(my_string)
    for i in indices:
        answer[i] = ' '
        
    str = ''.join(answer)
    str = str.replace(' ', '')
    return str