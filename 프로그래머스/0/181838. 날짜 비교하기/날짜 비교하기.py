def solution(date1, date2):
    sum1 = date1[0]*365 + date1[1]*365/12 + date1[2]
    sum2 = date2[0]*365 + date2[1]*365/12 + date2[2]
    return 1 if sum1 < sum2 else 0