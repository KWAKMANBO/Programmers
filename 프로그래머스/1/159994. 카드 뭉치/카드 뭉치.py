def solution(cards1, cards2, goal):
    answer = ""
    for i in goal:
        if len(cards1) >= 1 and i == cards1[0]:
            answer += cards1.pop(0)
        elif len(cards2) >= 1 and i == cards2[0]:
            answer += cards2.pop(0)
        else:
            return "No"
    return "Yes"