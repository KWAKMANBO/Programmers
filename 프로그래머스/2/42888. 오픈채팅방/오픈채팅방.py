def solution(record):
    answer = []
    users = {}
    for r in record:
        tmp = r.split()

        if tmp[0] == "Enter":
            users[tmp[1]] = tmp[2]
            answer.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == "Leave":
            answer.append([tmp[1], "님이 나갔습니다."])
        else:
            users[tmp[1]] = tmp[2]


    for a in answer:
        a[0] = users[a[0]] + a[1]

    return [a[0] for a in answer]

