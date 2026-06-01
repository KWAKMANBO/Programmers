def solution(book_time):
    answer = 0

    time_list = []

    for b in book_time:
        tmp = []
        for bb in b :
            h = int(bb[:2])
            m = int(bb[3:])
            tmp.append(60*h + m)

        tmp[1] +=10

        time_list.append(tmp)

    time_list.sort(key = lambda x : x[0])

    answer = [time_list[0]]
    for t in time_list[1:]:
        ns,ne = t
        for i in range(len(answer)):
            cs,ce = answer[i]
            if ce <= ns:
                answer[i] = t
                break
        else:
            answer.append(t)


    return len(answer)