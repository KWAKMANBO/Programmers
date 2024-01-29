def solution(order):
    answer = 0
    for i in order:
        if "cafelatte" in i:
            answer += 5000
        elif "americano" in  i:
            answer += 4500
        else:
            answer += 4500
        
    
    return answer