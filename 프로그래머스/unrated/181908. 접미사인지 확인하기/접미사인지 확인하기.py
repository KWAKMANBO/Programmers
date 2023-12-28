def solution(my_string, is_suffix):
    suffixs = []
    answer = 0
    for i in range(len(my_string)):
        suffixs.append(my_string[i:])
    if suffixs.count(is_suffix) == 1:
        return 1
    else:
        return 0