from collections import deque


def solution(order):
    answer = 0
    tmp_belt = deque([])
    belt = deque([i for i in range(1, len(order) + 1)])
    idx = 0
    # order의 idx    idx = 0  
    while True:
        # 컨테이너 벨트가 비어 있지 않고, 현재 order의 순서와 같은 상자라면  
        if belt and belt[0] == order[idx]:
            belt.popleft()
            answer += 1
            idx += 1
            # 임시 벨트의 가장 마지막 원소가 order의 순서와 같은 상자라면  
        elif tmp_belt and tmp_belt[-1] == order[idx]:
            tmp_belt.pop()
            answer += 1
            idx += 1
            # 현재 벨트의 맨앞 원소가 order와 다르다면 임시에 추가  
        elif belt and belt[0] != order[idx]:
            tmp_belt.append(belt.popleft())
            # belt와 tmp_belt가 둘다 비었따면  
        elif not belt and not tmp_belt:
            break
        else:
            break

    return answer