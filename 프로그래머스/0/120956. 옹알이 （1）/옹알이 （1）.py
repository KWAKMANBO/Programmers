def solution(babbling):
    answer = []
    arr = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        tmp = i
        for j in arr:
            tmp = tmp.replace(j, ' ')
        answer.append(tmp)

    for i in range(len(answer)):
         answer[i] =answer[i].replace(' ', '') 
        
    return answer.count('')