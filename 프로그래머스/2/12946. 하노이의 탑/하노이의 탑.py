def solution(n):
    answer = []

    # n 보내려는 원반의 숫자
    # source : 시작 기둥
    # target : 이동시켜야하는 목표 기둥
    # tmp : n-1을 세우기위한 임시로 거쳐가는 기둥
    def hanoi(num, source,target, tmp ):
        # 옮겨야 하는 원판이 1번 원판이면 그냥 옮기면됨
        if num == 1:
            answer.append([source,target])
            return

        # n-1개의 원판을 tmp 기둥으로 옮기기
        hanoi(num-1,source, tmp, target)

        # 마지막 남은 원판을 옮기기 즉, n원판을 target 기둥으로 옮김
        answer.append([source,target])

        # tmp에 있던 원판을 target로 옮기기
        hanoi(num-1, tmp,target,source)

    hanoi(n,1,3,2)



    return answer