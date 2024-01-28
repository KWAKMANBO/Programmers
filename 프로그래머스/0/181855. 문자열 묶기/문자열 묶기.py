def solution(strArr):
    answer = [len(i) for i in strArr]
    set_answer = set(answer)
    num_list = []
    for i in set_answer:
        num_list.append(answer.count(i))
    return max(num_list)