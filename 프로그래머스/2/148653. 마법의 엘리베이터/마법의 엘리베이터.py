def solution(storey):
    answer = 0

    while storey != 0:
        r = storey % 10
        if r > 10 - r:
            answer += 10 - r
            storey = storey // 10 + 1
        elif r < 10 - r:
            answer += r
            storey //= 10
        else:
            answer+=5
            if (storey % 100) // 10 >= 5:
                storey += r
            else:
                storey -= r



    return answer