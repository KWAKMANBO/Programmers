def solution(my_string):
    answer = [0 for i in range(52)]
    
    for i in range(len(my_string)):
        if ord(my_string[i]) < 91 and  ord(my_string[i]) > 64:
            # 대문자일때
            answer[ord(my_string[i])-65] +=1
        else:
            #소문자일때
            answer[ord(my_string[i])-71] +=1
    return answer