def solution(cap, n, deliveries, pickups):
    answer = 0

    deliv = 0
    pickup = 0

    for i in range(n - 1, -1, -1):
        deliv += deliveries[i]
        pickup += pickups[i]

        cnt = 0
        while deliv > 0 or pickup > 0:
            deliv -= cap
            pickup -= cap
            cnt += 1

        answer += (i + 1) * 2 * cnt
        
    return answer
