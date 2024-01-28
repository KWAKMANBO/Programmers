def solution(rank, attendance):
    enable_rank = []
    for idx,val in enumerate(rank):
        if attendance[idx] == True:
            enable_rank.append(val)

    enable_rank.sort()
    a = rank.index(enable_rank[0])
    b = rank.index(enable_rank[1])
    c = rank.index(enable_rank[2])
    print(a,b,c)
    return 10000*a + 100*b +c