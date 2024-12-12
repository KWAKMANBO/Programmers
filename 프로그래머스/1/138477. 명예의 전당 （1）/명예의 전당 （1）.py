def solution(k, score):
    answer = []
    lst = []
    for i in score:
        lst.append(i)
        lst = sorted(lst,reverse = True)
        answer.append(lst[k-1] if len(lst) > k else lst[-1])
    return answer