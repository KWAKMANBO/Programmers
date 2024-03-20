def solution(common):
    
    if common[1] - common[0] != common[2] - common[1]:
        # 공차가 서로 다르면 -> 공비수열
        r = common[1]/ common[0]
        return common[-1]*r
    else:
        d = common[1] - common[0]
        return common[-1] + d
    
