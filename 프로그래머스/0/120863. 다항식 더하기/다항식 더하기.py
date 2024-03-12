def solution(polynomial):
    num_x, num = 0, 0
    tmp = polynomial.split(" + ")
    for i in tmp:
        if i.isdigit():
            num +=int(i)
        else:
            if i == 'x':
                num_x += 1
            else:
                num_x += int(i[:-1])
    if num_x == 0 and num == 0:
        return "0"
    elif num_x == 0:
        return str(num)
    elif num_x == 1:
        if num == 0:
            return "x"
        return "x + "+ str(num)
    elif num == 0:
        return str(num_x) + "x"
    else:
        return str(num_x) +"x + " + str(num)