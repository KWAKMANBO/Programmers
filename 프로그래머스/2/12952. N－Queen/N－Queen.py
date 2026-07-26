def solution(n):
    answer = 0

    # pos[i] -> i는 row(행), pos[i]는 col(열)
    pos = [0] * n

    def check(row):
        # 0부터 row - 1까지 이전에 넣은 퀸들이 충돌하는게 있는지 검사
        for i in range(row):
            # i는 행을 pos[i]는 열을 의미하므로
            # pos[i]는 i번째 행의 pos[i]의 열에 퀸이 있음을 의미
            # pos[i] == pos[row]는 같은 열에 퀸이 있음을 의미하므로 False를 반환
            if pos[i] == pos[row]:
                return False

            # 대각선 확인
            # row와 i의 행의 차이와, 열의 차이가 같다면 즉 대각서에 있음을 의미함
            if abs(pos[i] - pos[row]) == abs(row - i):
                return False

        return True

    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return

        for i in range(n):
            pos[row] = i
            if check(row):
                dfs(row + 1)

    dfs(0)

    return answer