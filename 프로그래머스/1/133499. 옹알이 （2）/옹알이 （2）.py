def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for i in words:
        for j in range(len(babbling)):
            if i * 2 not in  babbling[j]:
                babbling[j] = babbling[j].replace(i, " ")

    for b in babbling:
        if b.isspace():
            answer += 1

    return answer