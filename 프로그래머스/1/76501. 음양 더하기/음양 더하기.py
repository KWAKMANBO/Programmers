def solution(absolutes, signs):
    answer = []
    for i,j in zip(absolutes, signs):
        if j == True:
            answer.append(i)
        else:
            answer.append(-1*i)
    
    return sum(answer)