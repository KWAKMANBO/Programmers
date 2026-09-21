def solution(cost, hint):
    answer = sum([c[0] for c in cost])
    ln = len(cost)

    # stage, hint_info, current_cost
    # 현재 스테이지, 힌트권 정보, 현재 비용
    def dfs(stage, hint_info, current_cost):
        nonlocal answer
        if stage == ln - 1:
            answer = min(answer, current_cost + cost[stage][hint_info[stage]])
            return

        # 힌트권 구매 안하는 경우 계산
        dfs(stage + 1, hint_info, current_cost + cost[stage][hint_info[stage]])

        # 힌트건 구매하는 경우 계산
        new_hint_info = hint_info[:]
        for h in hint[stage][1:]:
            new_hint_info[h - 1] += 1
            if new_hint_info[h - 1] == ln:
                new_hint_info[h - 1] = ln - 1

        dfs(stage + 1, new_hint_info, current_cost + cost[stage][hint_info[stage]] + hint[stage][0])

    dfs(0, [0] * (len(cost)), 0)
    return answer