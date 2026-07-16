def solution(plans):
    answer = []

    stack = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    for i in range(len(plans) - 1):

        title, st, t = plans[i]
        ntitle, nst, nt = plans[i + 1]

        # 이번 과제 종료시간이 다음 과제 시작 시간보다 작다면 완료
        if st + t <= nst:
            answer.append(title)
            time_diff = nst - (st + t)

            while time_diff != 0 and stack:
                tmp_title, tmp_st, tmp_time = stack.pop()
                if time_diff >= tmp_time:
                    answer.append(tmp_title)
                    time_diff -= tmp_time
                else:
                    stack.append([tmp_title, tmp_st, tmp_time - time_diff])
                    time_diff = 0
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])

    answer.append(plans[-1][0])

    while stack:
        answer.append(stack.pop()[0])

    return answer