def solution(dartResult):
    answer = 0
    before_num = 0
    num = []
    tmp = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            tmp += dartResult[i]
        else:
            if tmp != "":
                num.append(int(tmp))
                tmp = ""

        if dartResult[i] == "D":
            num[-1] **= 2
        elif dartResult[i] == "T":
            num[-1] **= 3
        elif dartResult[i] == "*":
            if len(num) == 1:
                num[-1] *= 2
            else:
                num[-1] *= 2
                num[-2] *= 2
        elif dartResult[i] == "#":
            num[-1] *= -1
    return sum(num)
