def solution(score):
    answer = []
    avg = []
    for i in score:
        avg.append(sum(i)/2)
    sort = sorted(avg,reverse = True)
    print(sort)
    for i in avg:
        answer.append(sort.index(i)+1)
        
            
    return answer