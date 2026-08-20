def solution(info, query):
    answer = []

    data = {}

    for i in info:
        ii = i.split()
        score = int(ii[4])

        lst = [ii[0], "-"]
        for k in ii[1:4]:
            tmp = []
            for l in lst:
                tmp.append(l + k)
                tmp.append(l + "-")
            lst = tmp
        for l in lst:
            if l not in data:
                data[l] = [score]
            else:
                data[l].append(score)

    for k in data:
        data[k].sort()

    for q in query:
        tmp = q.replace("and", "").split()
        qq = "".join(tmp[:-1])
        point = int(tmp[-1])

        if qq not in data:
            answer.append(0)
            continue

        nums = data[qq]
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid = (s + e) // 2
            if nums[mid] >= point:
                e = mid - 1
            else:
                s = mid + 1

        answer.append(len(nums) - s)
    return answer