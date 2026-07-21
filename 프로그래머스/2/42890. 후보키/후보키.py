from itertools import combinations


def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    unique = set()
    nums = [i for i in range(col_len)]
    col_combinations = []

    for i in range(1, col_len + 1) :
        col_combinations.extend(combinations(nums, i))

    for comb in col_combinations:
        # 최소성 검사
        is_minimal = True
        for u in unique:
            if set(u).issubset(set(comb)):
                is_minimal = False
                break
        if not is_minimal:
            continue

        rows = set()
        for r in relation:
            rows.add(tuple(r[c] for c in comb))

        if len(rows) == row_len:
            unique.add(comb)



    return len(unique)