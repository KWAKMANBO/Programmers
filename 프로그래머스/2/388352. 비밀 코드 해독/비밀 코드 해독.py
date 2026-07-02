from itertools import combinations


def solution(n, q, ans):
    answer = 0

    # 1부터 n까지의 숫자 중 5개를 고르는 모든 조합을 확인
    for com in combinations(range(1, n + 1), 5):
        # set으로 바꾸면 c in q[i] 연산이 더 빨라집니다.
        com_set = set(com)

        is_valid = True

        # 모든 질문(q)과 응답(ans)을 순회하며 검증
        for i in range(len(q)):
            # 현재 조합(com_set)과 질문한 코드(q[i])의 교집합 개수를 구함
            # 이 개수가 ans[i]와 정확히 일치해야 합니다 (ans[i]가 0인 경우도 포함)
            # cnt = len(com_set.intersection(q[i]))
            cnt = 0
            for c in com_set:
                if c in q[i]:
                    cnt += 1
            if cnt != ans[i]:
                is_valid = False
                break  # 하나라도 조건이 틀리면 더 볼 것도 없이 탈락

        if is_valid:
            answer += 1

    return answer