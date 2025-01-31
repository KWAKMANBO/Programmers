def solution(s):
    str_lst = s.split(" ")
    result = []
    for i in range(len(str_lst)):
        if str_lst[i]:
            result.append(str_lst[i][0].upper() + str_lst[i][1:].lower())
        else:
            result.append(str_lst[i])
    return " ".join(result)