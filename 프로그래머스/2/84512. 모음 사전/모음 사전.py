def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) // 4) * "AEIOU".index(word[i]) + 1
    return answer