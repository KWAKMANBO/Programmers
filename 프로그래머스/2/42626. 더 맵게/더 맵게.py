import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        tmp = first + (second*2)
        heapq.heappush(scoville, tmp)
        cnt +=1
        
         # heap의 원소가 1개이면서 K보다 작다면
        if len(scoville) == 1 and scoville[0] < K :
            return -1
        
        
    return cnt