def solution(numbers, direction):
    answer = []
    if direction == 'left':
        answer = numbers[1:]
        answer.append(numbers[0])
    else:
        answer.append(numbers[-1])
        answer.extend(numbers[0:-1])
    return answer