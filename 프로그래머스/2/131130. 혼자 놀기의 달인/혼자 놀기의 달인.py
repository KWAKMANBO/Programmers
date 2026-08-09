def solution(cards):
    answer = 0
    linked_list = {i + 1: cards[i] for i in range(len(cards))}

    ln = len(cards)
    tmp = {1}
    visited = {1}
    cnt = 0
    i = 1

    groups = []
    while cnt < ln:
        if linked_list[i] not in tmp:
            tmp.add(linked_list[i])
            visited.add(linked_list[i])
            i = linked_list[i]
        else:
            groups.append(tmp)
            tmp = set()
            for j in range(1, ln + 1):
                if j not in visited:
                    i = j
                    visited.add(j)
                    tmp.add(j)
                    break
        cnt += 1
    groups.sort(key=lambda x: len(x), reverse=True)

    return len(groups[0]) * len(groups[1]) if len(groups) != 1 else 0