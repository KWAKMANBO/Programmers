def solution(numbers):
    answer = []
    bin_numbers = []

    for n in numbers:
        if n % 2 == 0:
            bin_numbers.append(bin(n)[2:])
        if n % 2 == 1:
            bin_numbers.append("0" + bin(n)[2:])

    # 짝수
    # - 짝수는 무조건 맨마지막이 비트 1의자리 비트가 0 이므로 그냥 +1 해서 0을 1로 만들어주면됨
    # 홀수
    # - 홀수는 왼쪽부터 확인하면서 맨처음으로 만나는 01을 10으로 바꿔 주면됨

    for b in bin_numbers:
        if b[-1] == '0':
            tmp = b[:-1] + '1'
            answer.append(int(tmp, 2))
        else:
            tmp = b
            for i in range(len(b) - 1, 0, -1):
                if tmp[i - 1: i + 1] == "01":
                    tmp = tmp[:i-1] + "10" + tmp[i + 1:]
                    answer.append(int(tmp, 2))
                    break


    return answer