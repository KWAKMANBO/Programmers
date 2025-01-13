def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    # code = 0 , date = 1, maximum = 2, remain = 3
    lst = []
    dic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for d in data:
        print(d[dic[ext]])
        if d[dic[ext]] < val_ext:
            lst.append(d)

    lst.sort(key=lambda x: x[dic[sort_by]])

    return lst