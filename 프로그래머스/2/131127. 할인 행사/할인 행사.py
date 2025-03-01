def solution(want, number, discount):
    answer = 0
    index_dict = {}

    for i in range(len(want)):
        index_dict[want[i]] = i
    for i in range(len(discount) - 10 + 1):
        tmp = [0] * len(want)
        for j in range(i, i + 10):
            if index_dict.get(discount[j]) is not None:
                tmp[index_dict[discount[j]]] += 1


        if number == tmp:
            answer += 1

    return answer