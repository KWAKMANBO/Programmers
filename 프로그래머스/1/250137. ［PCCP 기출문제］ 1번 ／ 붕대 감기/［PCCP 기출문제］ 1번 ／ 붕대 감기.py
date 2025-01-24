# bandage : [기술의 시전 시간 ,1초당 회복량, 추가 회복량]
# health : 최대 체력을 의미
# attacks : [공격 시간, 피해량]
def solution(bandage, health, attacks):
    answer = health
    answer -= attacks[0][1]
    if answer < 1:
        return -1

    for i in range(1, len(attacks)):
        t = attacks[i][0] - attacks[i - 1][0] - 1

        answer = answer + bandage[1] * t if answer + bandage[1] * t < health else health

        if t >= bandage[0]:
            answer = answer + bandage[2]*(t//bandage[0]) if answer + bandage[2]*(t//bandage[0]) < health else health
        answer -= attacks[i][1]
        if answer <= 0:
            return -1

    return answer if answer > 0 else -1

