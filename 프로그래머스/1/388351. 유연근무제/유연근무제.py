def solution(schedules, timelogs, startday):
    answer = 0
    # 출른 희망 시각 + 10분 계산
    for i in range(len(schedules)):
        schedules[i] = ((schedules[i] // 100) + (((schedules[i] % 100) + 10) // 60)) * 100 + (
                schedules[i] % 100 + 10) % 60
    for s in range(len(schedules)):
        check = False
        for i in range(7):
            currentDay = ((startday - 1) + i) % 7

            if currentDay != 5 and currentDay != 6:
                if timelogs[s][i] > schedules[s]:
                    check = not check
                    break
        if not check:
            answer += 1

    return answer