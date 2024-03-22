def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name,yearning))
    
    for i in photo:
        sum = 0 
        for person in i:
            if person in score.keys():
                sum += score[person]
        
        answer.append(sum)
            
    
    return answer