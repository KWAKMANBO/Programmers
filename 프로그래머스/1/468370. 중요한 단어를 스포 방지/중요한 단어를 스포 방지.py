def solution(message, spoiler_ranges):
    spoiler_words = []
    no_spoiler_words = []
    idx = 0
    for w in message.split():
        s = message.index(w, idx)
        e = s + len(w) - 1
        idx = e + 1

        is_spoiler = False
        for i in spoiler_ranges:
            ss, ee = i[0], i[1]
            if s <= ee and e >= ss:
                spoiler_words.append(w)
                is_spoiler = True
                break

        if not is_spoiler:
            no_spoiler_words.append(w)

    answer = set()
    for sw in spoiler_words:
        if sw not in no_spoiler_words:
            answer.add(sw)
    return len(answer)