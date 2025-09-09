import heapq


#  번호를 순서대로 할 필요없음이 중요
#  적은 시간을 가지 음식부터 번호 매기기
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 총 소요한 시간
    sum_value = 0
    # 이전 푸드의 소요시간
    previous = 0
    length = len(food_times)
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value = sum_value + (now - previous) * length
        length -= 1
        previous = now

    q.sort(key=lambda x: x[1])
    return q[(k - sum_value) % length][1]
