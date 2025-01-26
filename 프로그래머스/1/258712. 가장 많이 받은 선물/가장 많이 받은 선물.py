# 선물 기록 O -> 선물을 더 많이 준 사람이 다음달에 받음
# 선물 기록 X or 주고 받은 기록이 smae-> 선물 지수가 더큰 사람이 받기
# 선물 지수는 내가 준 선물 - 받은 선물
# 지수가 같다면 선물 x
def solution(friends, gifts):
    answer = 0

    gift_record = [[0 for i in range(len(friends))] for _ in range(len(friends))]
    new_gift = [0] * len(friends)
    gift_score = [0] * len(friends)
    # 선물보낸 기록 기록하기
    for g in gifts:
        sender, receiver = g.split()
        gift_record[friends.index(sender)][friends.index(receiver)] += 1

    # 선물 지수계산
    for f in friends:
        send_cnt = sum(gift_record[friends.index(f)])
        received_cnt = 0
        for i in gift_record:
            received_cnt += i[friends.index(f)]
        gift_score[friends.index(f)] = send_cnt - received_cnt

    for i in range(len(gift_record)):
        for j in range(len(gift_record[0])):
            if i != j:
                if gift_record[i][j] > gift_record[j][i]:
                    new_gift[i] += 1
                elif gift_record[i][j] == gift_record[j][i]:
                    if gift_score[i] > gift_score[j]:
                        new_gift[i] += 1
    
    return max(new_gift)