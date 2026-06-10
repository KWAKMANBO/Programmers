import math


def solution(signals):
    answer = 0
    # 각 신호등의 주기를 저장할 배열
    periods = [0] * len(signals)
    # 신호등의 상태를 계산할 최소 시간 -> 이 이후로는 패턴이 반복됨
    MAX_SECOND = 1

    # periods초기화 및 MAX_SECOND계산
    for i in range(len(signals)):
        # 주기를 계산
        periods[i] = sum(signals[i])
        # MAX_SECOND를 계산
        MAX_SECOND = math.lcm(MAX_SECOND, periods[i])

    yellows = []

    for i in range(len(signals)):
        tmp = [0] * periods[i]
        # 초록불과 노란불 사이를 1로 할당해 노란불임을 표시
        for j in range(signals[i][0], signals[i][0] + signals[i][1]):
            tmp[j] = 1

        yellows.append(tmp)

    for t in range(1, MAX_SECOND):

        all_yellow_flag = True
        for i in range(len(signals)):
            idx = (t - 1) % periods[i]
            if yellows[i][idx] != 1:
                all_yellow_flag = False
                break
        if all_yellow_flag:
            return t

    return -1

    return answer