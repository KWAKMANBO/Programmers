def solution(my_string, overwrite_string, s):
    answer = ''

    answer = my_string[0:s] + overwrite_string[0:len(overwrite_string)] + my_string[s+len(overwrite_string): len(my_string)]
    print(answer)
   
    return answer