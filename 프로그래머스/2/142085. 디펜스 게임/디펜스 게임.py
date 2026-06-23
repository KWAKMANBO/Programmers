import heapq


def solution(n, k, enemy):
    answer = 0
    hq = []
    for e in enemy:

        # 일단 적을 빼기
        n -= e
        heapq.heappush(hq, -e)

        # 적을 뺴고 난 후 내 병사에서 감당할 수 없다면
        if n < 0:
            if k > 0:
                # 무적권을 사용
                n += -1*heapq.heappop(hq)
                k -= 1
            else:
                break

        answer += 1

    return answer