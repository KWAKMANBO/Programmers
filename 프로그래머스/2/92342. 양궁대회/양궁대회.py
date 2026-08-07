def solution(n, info):
    max_gap = 0
    answer = [-1]

    def find_winner_and_calculate_point_diff(apeach, ryan):
        a, r = 0, 0
        for i in range(11):
            if apeach[i] == 0 and ryan[i] == 0:
                continue
            if apeach[i] >= ryan[i]:
                a += 10 - i
            else:
                r += 10 - i
        return (True, r-a) if r > a else (False, a-r)

    def compare_list(a, b):
        for i in range(10, -1, -1):
            if a[i] > b[i]:          # ← 수정
                return a
            elif a[i] < b[i]:
                return b
        return b

    def dfs(index, arrows_left, ryan):
        nonlocal max_gap, answer
        if index == 10:
            ryan[10] = arrows_left
            winner, gap = find_winner_and_calculate_point_diff(info, ryan)
            if winner and gap > max_gap:
                max_gap = gap
                answer = ryan[:]
            elif winner and gap == max_gap:
                answer = compare_list(ryan[:], answer)   # ← 수정
            ryan[10] = 0
            return

        if arrows_left == 0:
            winner, gap = find_winner_and_calculate_point_diff(info, ryan)
            if winner and gap > max_gap:
                max_gap = gap
                answer = ryan[:]
            elif winner and gap == max_gap:
                answer = compare_list(ryan[:], answer)   # ← 수정
            return

        need = info[index] + 1
        dfs(index + 1, arrows_left, ryan)
        if arrows_left >= need:
            ryan[index] = need
            dfs(index + 1, arrows_left - need, ryan)
            ryan[index] = 0

    dfs(0, n, [0]*11)
    return answer