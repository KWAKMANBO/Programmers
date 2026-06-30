# 이분 탐색으로 해보자
def solution(diffs, times, limit):
    start = min(diffs)
    end = max(diffs)
    while start <= end:
        level = (start + end) // 2
        tmp = times[0]
        for i in range(1, len(diffs)):
            diff = diffs[i]
            time_prev = times[i - 1]
            time_cur = times[i]

            if diff > level:
                tmp += (diff - level) * (time_cur + time_prev) + time_cur
            else:
                tmp += time_cur
        if tmp <= limit:
            answer = level
            end = level - 1
        else:
            start = level + 1

    return answer