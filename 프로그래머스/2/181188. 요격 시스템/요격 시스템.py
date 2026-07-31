def solution(targets):
    answer = 1
    # 작성하신 정렬 기준 그대로 유지
    targets.sort(key=lambda x: (x[0], x[1]))

    # 작성하신 find 함수를 교집합 공식으로 수정
    def find(a, b):
        start = max(a[0], b[0])
        end = min(a[1], b[1])

        # 시작점이 끝점보다 작아야 겹치는 구간이 존재함 (개구간 조건)
        if start < end:
            return [start, end]
        else:
            return [-1, -1]

    tmp = targets[0]
    for t in targets[1:]:
        c = find(tmp, t)
        if c != [-1, -1]:
            tmp = c  # 겹치는 공통 구간으로 좁힘
        else:
            answer += 1
            tmp = t  # 새로운 구간 시작

    return answer
