def solution(chicken):
    answer = 0
    coupon = 0
    while chicken >= 10:
        # 서비스 받을 치킨 수 뺴고 나머지 쿠폰수를 저장
        coupon = chicken % 10
        chicken = chicken // 10
        answer += chicken
        chicken += coupon
    return answer