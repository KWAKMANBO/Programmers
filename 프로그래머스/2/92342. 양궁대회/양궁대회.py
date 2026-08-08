def solution(n, info):
    answer = [-1] 
    max_gap = 0

    # 승자 확인 및 점수 차이 계산
    def get_winner_and_diff(ap, ry):
        a, r = 0, 0,

        for i in range(11):
            if ap[i] == 0 and ry[i] == 0:
                continue

            if ry[i] > ap[i]:
                r += 10 - i
            else:
                a += 10 - i
        return r > a, r - a

    # 배열 비교 사용할 배열 결정
    def compare_list(current, new):
        for i in range(10, -1, -1):
            if current[i] > new[i]:
                return current
            elif current[i] < new[i]:
                return new

        return current

    # 백트랙킹(DFS)
    def dfs(index, arrow_left, ryan):
        nonlocal answer, max_gap

        if index == 10:
            ryan[10] = arrow_left
            winner, gap = get_winner_and_diff(info, ryan)
            if winner and gap > max_gap:
                max_gap = gap
                answer = ryan[:]
            elif winner and gap == max_gap:
                answer = compare_list(answer, ryan[:])
            ryan[10] = 0
            return
        if arrow_left == 0:
            winner, gap = get_winner_and_diff(info, ryan)
            if winner and gap > max_gap:
                max_gap = gap
                answer = ryan[:]
            elif winner and gap == max_gap:
                answer = compare_list(answer, ryan[:])

            return

        needed = info[index] + 1
        dfs(index + 1, arrow_left, ryan)

        if arrow_left >= needed:
            ryan[index] = needed
            dfs(index + 1, arrow_left - needed, ryan)
            ryan[index] = 0


    dfs(0, n, [0] * 11)

    return answer


