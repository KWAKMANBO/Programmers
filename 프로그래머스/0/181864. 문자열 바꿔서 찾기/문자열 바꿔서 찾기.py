def solution(myString, pat):
    change = ""
    for i in myString:
        if i == 'A':
            change += 'B'
        else:
            change += 'A'

    if pat in change:
        return 1
    else:
        return 0