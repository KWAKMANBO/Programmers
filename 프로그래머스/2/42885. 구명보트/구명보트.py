def solution(people, limit):
    answer = 0
    s, e = 0, len(people) - 1
    people.sort()
    while s <= e:
        if people[s] + people[e] <= limit:
            answer += 1
            s += 1
            e -= 1
        elif people[s] + people[e] > limit:
            e -= 1
            answer += 1

    return answer