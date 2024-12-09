def solution(sizes):
    w_lst = []
    h_lst = []
    for i in sizes:
        if i[0] < i[1]:
            w_lst.append(i[1])
            h_lst.append(i[0])
        else:
            w_lst.append(i[0])
            h_lst.append(i[1])
    return max(w_lst)*max(h_lst)

