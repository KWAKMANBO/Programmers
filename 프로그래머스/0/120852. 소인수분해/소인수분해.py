def solution(n):
    answer = []
    div = 2
    while n > 1:
        if n % div == 0:
            #n이 div의 배수라면
            n = n // div
            if div not in answer:
                answer.append(div)
        else:
            div +=1
    return answer