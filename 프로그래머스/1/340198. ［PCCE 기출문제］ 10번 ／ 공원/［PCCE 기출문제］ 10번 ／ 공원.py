# 돗자리 배치가 가능한지 확인하는 함수
def valid_check(mat, park, row, col):
    for r in range(row, row + mat):
        for c in range(col, col + mat):
            # 범위가 벗어나지 않게 조절
            if r < len(park) and c < len(park[0]):
                if park[r][c] != "-1":
                    return False
            else:
                return False
    return True


def solution(mats, park):
    answer = 0

    # 돗자리느 정사각형
    # 돗자리가 들어갈 수 있는자리가 있는지 확인하기
    mats = sorted(mats, reverse=True)
    for m in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if valid_check(m, park, i, j):
                    return m

    return -1