def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(0)
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
            if j == len(prices)-1:
                answer[i] = j - i
    return answer