from collections import deque


# bridge_length는 다리에 올라갈 수 있는 자동차 최대 대수
# weight는 다리 최대 무게
# truck_weights는 대기 트럭
def solution(bridge_length, weight, truck_weights):
    time = 0

    trc = deque(truck_weights)
    brd = deque()
    passed = 0
    ln = len(truck_weights)

    def count_weight(brd):
        w = 0
        for b in brd:
            w += b[0]
        return w

    while passed < ln:
        for b in brd:
            b[1] += 1

        if brd and brd[0][1] >= bridge_length:
            brd.popleft()
            passed += 1

        time += 1

        if trc and count_weight(brd) + trc[0] <= weight and len(brd) != bridge_length:
            brd.append([trc.popleft(), 0])



    return time
