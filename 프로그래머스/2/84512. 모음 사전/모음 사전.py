from itertools import product


def solution(word):
    chrs = ['A', 'E', 'I', 'O', 'U']
    word = tuple(word)
    answer = []
    for i in range(5):
        for w in product(chrs, repeat=i + 1):
            answer.append(w)
    answer.sort()
    return answer.index(word) + 1