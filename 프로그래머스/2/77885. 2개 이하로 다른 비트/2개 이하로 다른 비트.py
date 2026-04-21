def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            bin_n = bin(n)[2:][::-1]
            bin_n = bin_n + "0"
            for i in range(len(bin_n)):
                if bin_n[i:i+2] == "10":
                    bin_n = bin_n[:i] + "01" + bin_n[i+2:]
                    break
            answer.append(int(bin_n[::-1],2))


    return answer