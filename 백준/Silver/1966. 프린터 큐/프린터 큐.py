import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


def check_priority(priority, queue):
    max_p = 0
    for doc in queue:
        max_p = max(doc[1], max_p)
    return priority >= max_p


for _ in range(N):
    # n은 원소의 개수
    # m은 찾고자 하는 원소의 순서
    # index는 0에서 시작
    n, m = map(int, input().split())
    queue = deque()
    max_priority = 0
    for i, s in enumerate(input().split()):
        int_s = int(s)
        queue.append([i, int_s])
    cnt = 0
    while True:
        idx, priority = queue.popleft()
        if check_priority(priority,queue):
            cnt+=1
            if idx == m :
                break
        else:
            queue.append([idx, priority])
    print(cnt)
