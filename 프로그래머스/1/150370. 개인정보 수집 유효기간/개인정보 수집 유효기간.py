def solution(today, terms, privacies):
    answer = []
    # today로부터 연,월,일 추출
    ty, tm, td = map(int, today.split("."))

    # terms을 dic으로 변환
    terms_dic = {}
    for t in terms:
        alph, month = t.split(" ")
        terms_dic[alph] = int(month)
    # 비교로직
    for i in range(len(privacies)):
        register_day, alph = privacies[i].split(" ")
        py, pm, pd = map(int, register_day.split('.'))
        months = terms_dic[alph]
        exp_y = py + months // 12
        months = months % 12
        exp_m = pm + months
        if exp_m > 12:
            exp_y += 1
            exp_m %= 12
        if pd == 1:
            exp_m -= 1
        exp_d = pd - 1 if pd > 1 else 28


        # 연도가 넘은 경우
        if ty > exp_y:
            answer.append(i + 1)
        elif ty == exp_y and tm > exp_m:
            # 월이 넘은 경우
            answer.append(i + 1)
        elif ty == exp_y and tm == exp_m and td > exp_d:
            # 일이 넘은 경우
            answer.append(i + 1)

    return answer