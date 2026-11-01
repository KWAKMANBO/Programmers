def solution(edges):
    answer = [0, 0, 0, 0]

    in_degrees = {}
    out_degrees = {}

    for s, e in edges:
        if s not in in_degrees:
            in_degrees[s] = 0

        if e not in in_degrees:
            in_degrees[e] = 0

        if s not in out_degrees:
            out_degrees[s] = 0

        if e not in out_degrees:
            out_degrees[e] = 0

        out_degrees[s] += 1
        in_degrees[e] += 1

    new_node = [0, 0]

    for k in out_degrees:
        if out_degrees[k] > new_node[1] and in_degrees[k] == 0:
            new_node = [k, out_degrees[k]]
    answer[0] = new_node[0]


    for k in in_degrees:
        # 도넛 모양
        if k != new_node[0] and out_degrees[k] == 2:
            answer[3] += 1

        # 막대 모양
        if out_degrees[k] == 0:
            answer[2] += 1
    answer[1] = new_node[1] - (answer[2] + answer[3])

    return answer
