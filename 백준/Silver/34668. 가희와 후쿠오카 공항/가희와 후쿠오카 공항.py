# 1. 국제선 -> 국내선 : 4분 소요
# 2. 국내선 정차 : 2분 소요
# 3. 국내선 -> 국제선 : 4분 소요
# 4. 국제선 정차 : 2분 소요
# 5. 현재 시간 > 막차 시간 -> 운행 종료

# 목표 : 가회가 몇시에 국내선을 타나?



# 336명
# 국내선 -> 국제선 +4분
# 정차 +2분
# 국제선 ->  국내선 +4분
# 정차 +2분
# 왕복 12분
# 336 -> 6.X -> 6 * 12 = 72



Q = int(input())

for i in range(Q):
    answer_hour = 6
    answer_minute = 0
    people = int(input())
    time = (people//50)*12 + 6
    answer_hour += time//60
    answer_minute += time % 60
    print(f"{str(answer_hour).zfill(2)}:{str(answer_minute).zfill(2)}")

