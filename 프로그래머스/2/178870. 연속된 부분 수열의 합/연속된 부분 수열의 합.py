def solution(sequence, k):
    answer = [0, 100000001]

    tmp = sequence[0]
    s, e = 0, 0
    while s <= e and e < len(sequence):
        # print(f"s : {s}, e: {e}, tmp : {tmp}" )
        if tmp < k:
            e += 1
            if e == len(sequence):
                break
            tmp += sequence[e]
        elif tmp > k:
            tmp -= sequence[s]
            s += 1
        else:
            # print(f"------ same ------")
            # print(f"s : {s}, e: {e}, tmp : {tmp}")
            # print(f"e - s : {e-s}, answer[1] - answer[0]: {answer[1] - answer[0]} ")
            if e - s < answer[1] - answer[0]:
                print("Dddd")
                answer = [s, e]
            # print(f"answer : {answer}")
            # print(f"------------------")
            tmp -= sequence[s]
            s += 1
    return answer


#print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2],6))