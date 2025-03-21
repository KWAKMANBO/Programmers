from itertools import permutations


def solution(k, dungeons):
    answer = -1

    nPr = permutations(dungeons, len(dungeons))

    for n in nPr:
        cnt = 0
        f = k
        for j in n:
            if f >= j[0]:
                f -= j[1]
                cnt += 1

        answer = max(answer, cnt)

    return answer