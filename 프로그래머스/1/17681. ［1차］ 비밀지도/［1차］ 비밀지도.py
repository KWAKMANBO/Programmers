def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        b1 = format(arr1[i], f"0{n}b")
        b2 = format(arr2[i], f"0{n}b")
        tmp = ""
        for j in range(n):
            if b1[j] == "0" and b2[j] == "0":
                tmp += " "
            else:
                tmp += "#"
        answer.append(tmp)
    return answer