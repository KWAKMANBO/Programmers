N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

wall_cnt = 0
one_way_virus = 0
all_way_virus = 0
vaccine = 0
start = 0
end = 0
for b in board:
    wall_cnt += b.count("#")
    one_way_virus += b.count("U") + b.count("D") + b.count("L") + b.count("R")
    all_way_virus += b.count("A")
    vaccine += b.count("V")
    start += b.count("S")
    end += b.count("E")
# print(f"wall_cnt : {wall_cnt}, one_way_virus : {one_way_virus}, all_way_virus : {all_way_virus}, vaccine : {vaccine}")
answer = -1

if start == 1 and end == 1:
    if wall_cnt < 2 and one_way_virus < 2 and all_way_virus == 0 and vaccine == 0:
        answer = 1
    elif all_way_virus == 0 and vaccine == 0:
        answer = 2
    elif all_way_virus == 0:
        answer = 3
    else:
        answer = 4

print(answer)
