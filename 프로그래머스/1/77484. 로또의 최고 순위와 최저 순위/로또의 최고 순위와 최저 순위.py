def solution(lottos, win_nums):
    min_win = 0
    max_win = 0
    win = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    zero_cnt = lottos.count(0)
    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
    print(cnt)
    answer = [win[cnt + zero_cnt],win[cnt]]
    return answer