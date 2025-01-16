def solution(numbers, hand):
    answer = ''
    l = [3, 0]
    r = [3, 2]
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            l = dic[n]
            answer += 'L'
        elif n == 3 or n == 6 or n == 9:
            r = dic[n]
            answer += 'R'
        else:
            rr = abs(dic[n][0] - r[0]) + abs(dic[n][1] - r[1])
            ll = abs(dic[n][0] - l[0]) + abs(dic[n][1] - l[1])
            if rr == ll:
                answer += "R" if hand == "right" else "L"
                if hand == "right":
                    r = dic[n]
                else:
                    l = dic[n]
            elif rr > ll:
                l = dic[n]
                answer += 'L'
            else:
                r = dic[n]
                answer += "R"

    return answer