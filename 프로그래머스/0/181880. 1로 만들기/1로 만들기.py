def solution(num_list):
    answer = 0
    for i in num_list:
        while True:
            if i == 1:
                # if i is 1 quit loop
                break
            elif i % 2 == 0:
                # if i is even number
                answer += 1
                i = int(i/2)
            elif i % 2 == 1:
                # if i is odd number
                answer += 1
                i = int((i - 1)/2)

    return answer