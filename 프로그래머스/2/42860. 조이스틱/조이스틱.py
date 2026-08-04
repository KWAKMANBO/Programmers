def solution(name):
    answer = 0

    # 알파벳 바꾸는 최소 횟수 구하기
    for n in name:
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
    ln = len(name)

    min_move = ln - 1
    # 커서 이동 횟수
    for i in range(ln):
        next_i = i + 1
        while next_i < ln and name[next_i] == 'A':
            next_i += 1
        min_move = min(min_move, 2*i + 1 + ln - 1 - next_i, 2*(ln - 1-next_i) + 2 + i )

    answer += min_move

    return answer