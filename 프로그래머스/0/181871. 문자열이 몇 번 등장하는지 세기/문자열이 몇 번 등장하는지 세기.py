def solution(myString, pat):
    start = 0
    cnt = 0

    while True:
        # find함수는 찾고자 하는 문자열이 없으면
        # -1을 반환
        idx = myString.find(pat, start)

        if idx == -1:
            break

        cnt += 1
        start = idx + 1
        # find를 통해 찾은 인덱스 +1 을 start로 설정

    return cnt
