def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in skip:
        alphabet = alphabet.replace(i, "")

    answer = ""

    for i in s:
        answer += alphabet[(alphabet.index(i) + index) % len(alphabet)]

    return answer