def solution(nums):
    pick = len(nums)/2
    set_arr = set(nums)
    # 뽑아야되는 종류의수가 총 포켓몬의 종류의 수보다 크다면
    if pick >= len(set_arr):
        return len(set_arr)
    else:
        return pick