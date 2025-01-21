def solution(id_list, report, k):
    answer = []
    id_dic = {}
    report_name = {}
    for id in id_list:
        id_dic[id] = 0
        report_name[id] = []
    report_set = set(report)
    for r in report_set:
        name1, name2 = r.split(" ")
        report_name[name1].append(name2)
        id_dic[name2] += 1
    for id in id_list:
        cnt = 0
        for n in report_name[id]:
            if id_dic[n] >= k:
                cnt += 1
        answer.append(cnt)

    return answer