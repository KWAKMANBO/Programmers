def solution(places):
    answer = []

    def check(place):

        for i in range(5):
            for j in range(5):
                # 오른쪽, 아래, 대각선 확인하기
                if place[i][j] == 'P':
                    # 바로 옆 오른쪽 확인
                    if j < 4 and place[i][j + 1] == 'P':
                        return False
                    # 바로 아래쪽 확인
                    if i < 4 and place[i + 1][j] == 'P':
                        return False

                    # 맨해튼 거리 2인 경우 확인

                    # 오른쪽 인 경우 확인
                    if j < 3 and place[i][j + 2] == 'P' and place[i][j + 1] != 'X':
                        return False
                    # 아래인 경우 확인
                    if i < 3 and place[i + 2][j] == 'P' and place[i + 1][j] != 'X':
                        return False
                    # 오른쪽 대각선인 경우 확인
                    if i < 4 and j < 4 and place[i + 1][j + 1] == 'P' and (
                            place[i + 1][j] != 'X' or place[i][j + 1] != 'X'):
                        return False
                    # 왼쪽 대각선인 경우 확인
                    # i + 1, j -1
                    if i < 4 and j > 0 and place[i + 1][j - 1] == 'P' and (
                            place[i][j - 1] != 'X' or place[i + 1][j] != 'X'):
                        return False
        return True

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


