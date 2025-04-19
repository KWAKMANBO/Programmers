def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(0)
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer