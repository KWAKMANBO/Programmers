def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0 :
            # if i is even number
            answer.append(strArr[i].lower())
        else:
            # if i is odd number
            answer.append(strArr[i].upper())

    return answer