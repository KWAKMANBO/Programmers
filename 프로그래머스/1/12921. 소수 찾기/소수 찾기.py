def solution(n):
    answer = 0
    for j in range(2, n+1):   
        for i in range(2, int((j**0.5)) + 1):    
            if j % i == 0 :
                answer +=1
                break
    return (n - 1) - answer