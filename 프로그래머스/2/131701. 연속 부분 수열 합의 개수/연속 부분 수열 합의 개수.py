def solution(elements):
    answer = set()
    elements *= 2

    for i in range(len(elements) // 2):
        for j in range(i+1, i + len(elements) // 2 + 1):
            answer.add(sum(elements[i:j]))

    return len(answer)