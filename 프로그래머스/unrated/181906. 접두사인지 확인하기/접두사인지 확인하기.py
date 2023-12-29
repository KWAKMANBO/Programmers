def solution(my_string, is_prefix):
    prefixs = []
    answer = 0
    for i in range(len(my_string)):
        prefixs.append(my_string[0:len(my_string)-i])
    
    if prefixs.count(is_prefix) > 0 :
        return 1
    else:
        return 0