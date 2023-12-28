def solution(my_string):
    suffixs = []
    answer = []
    for i in range(len(my_string)):
        suffixs.append(my_string[i:])
    suffixs.sort()
    return suffixs
