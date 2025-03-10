
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for c in clothes:
        if not clothes_dict.get(c[1]):
            clothes_dict[c[1]] = [c[0]]
        else:
            clothes_dict[c[1]].append(c[0])
    lst = [len(clothes_dict[i]) for i in clothes_dict.keys()]

    for l in lst:
        answer*=(l+1)


    return answer-1