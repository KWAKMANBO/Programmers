import heapq


#  번호를 순서대로 할 필요없음이 중요
#  적은 시간을 가지 음식부터 번호 매기기
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    hq = []
    for i in range(length):
        heapq.heappush(hq, (food_times[i], i + 1))

    spending_time = 0
    previous_time = 0

    while spending_time + (hq[0][0] - previous_time) * length <= k:
        now = heapq.heappop(hq)
        spending_time += (now[0] - previous_time) * length
        length = len(hq)
        previous_time = now[0]

    hq.sort(key=lambda x: x[1])
    return hq[(k - spending_time) % length][1]