def solution(emergency):
    answer = []
    tmp = [i for i in emergency]
    dict = {}
    emergency.sort(reverse=True)
    for i in range(len(emergency)):
        dict[emergency[i]] = i + 1
        
    print(emergency)
    print(tmp)
    print(dict)
    for i in range(len(tmp)):
        answer.append(dict[tmp[i]])    
    return answer