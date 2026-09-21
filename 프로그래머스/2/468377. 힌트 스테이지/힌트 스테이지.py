def solution(cost, hint):
    answer = sum(c[0] for c in cost)
    ln = len(cost)

    # cost -> 0 based이니
    # hint info도 0base로 맞추자
    def dfs(stage, hint_info, current_cost):
        nonlocal answer
        if stage == ln - 1:
            answer = min(answer, current_cost + cost[stage][hint_info[stage]])
            return
            # hint권을 구매하지 않고 스테이지를 클리어한 경우
        dfs(stage + 1, hint_info, current_cost + cost[stage][hint_info[stage]])

        # hint권을 구매한 후 스테이지를 클리어한 경우
        new_hint_info = hint_info[:]
        for h in hint[stage][1:]:
            new_hint_info[h - 1] += 1
            if new_hint_info[h-1] == ln:
                new_hint_info[h-1] = ln - 1

        dfs(stage + 1, new_hint_info, current_cost + cost[stage][hint_info[stage]] + hint[stage][0])

    dfs(0, [0] * ln, 0)

    return answer