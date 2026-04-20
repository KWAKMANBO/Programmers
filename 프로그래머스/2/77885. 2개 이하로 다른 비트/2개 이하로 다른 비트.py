def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            tmp = bin(n)[2:]
            tmp = tmp.zfill(len(tmp) + 1)
            for i in range(len(tmp) - 1, -1, -1):

                if tmp[i - 1: i + 1] == "01":
                    #print(f"tmp[{i - 1} : {i + 1}] : {tmp[i - 1: i + 1]}")
                    tmp = tmp[:i-1] + "10" + tmp[i+1:]
                    break
            answer.append(int(tmp,2))

    return answer