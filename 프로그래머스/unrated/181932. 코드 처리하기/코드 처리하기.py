def solution(code):
    mode = 0
    answer = ''
    for idx in range(len(code)):
        if mode == 0 and idx % 2 == 0 and code[idx] != '1':
            answer += code[idx]
        elif code[idx] == '1':
            if mode == 0 :
                mode = 1
            else :
                mode = 0
        elif mode == 1 and idx % 2 == 1 and code[idx] != '1':
            answer += code[idx]
        
            
    if answer == '':    
        return 'EMPTY'
    else :
        return answer