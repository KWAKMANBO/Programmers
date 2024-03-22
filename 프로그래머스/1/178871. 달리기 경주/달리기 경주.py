def solution(players, callings):
    answer = []
    rank = {}
    for idx,name in enumerate(players):
        rank[name] = idx
    
    for i in callings:
        idx = rank[i]
        
        players[idx],players[idx-1] = players[idx-1],players[idx]
        
        rank[i] -=1
        rank[players[idx]] +=1
    
    return players