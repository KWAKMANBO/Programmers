def solution(files):
    f_lst = []
    for f in files:
        num_s, num_e = 0, 0
        for j in range(len(f)):
            if f[j].isdigit():
                num_s = j
                break

        for j in range(num_s, len(f)):
            if not f[j].isdigit():
                num_e = j
                break
        else:
            num_e = len(f)

        head = f[:num_s].lower()
        number = int(f[num_s:num_e])
        tail = f[num_e:]

        f_lst.append([head, number, tail, f])
    f_lst.sort(key=lambda x: (x[0], x[1]))

    return [f[3] for f in f_lst]
