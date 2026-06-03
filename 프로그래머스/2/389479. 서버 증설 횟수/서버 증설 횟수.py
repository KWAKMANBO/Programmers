def solution(players, m, k):
    answer = 0
    servers = {}
    current_server = 0
    for i in range(len(players)):

        if i in servers.keys():
            current_server -= servers[i]

        p = players[i]
        s = p // m

        diff = 0
        if s > current_server :
            diff = s - current_server
            current_server += diff
            servers[i + k] = diff
            answer += diff
        

    return answer