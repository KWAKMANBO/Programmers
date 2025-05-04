import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 캐릭터의 좌표와 방향을 입력받기
x, y, direction = map(int, input().split())

d[x][y] = 1

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북,동,남,서 방향 정의하기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전하는 함수
def ture_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    ture_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        # 회전한 이후 정면에 가보지 않은 칸이 없거나, 바다인 경우
        turn_time +=1
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                # 뒤가 바다로 막혀 있는 경우
                break
            turn_time = 0
print(count)
