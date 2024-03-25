def solution(numbers):
    answer = [i for i in range(0,10)]
    for i in numbers:
        answer.remove(i)
    return sum(answer)