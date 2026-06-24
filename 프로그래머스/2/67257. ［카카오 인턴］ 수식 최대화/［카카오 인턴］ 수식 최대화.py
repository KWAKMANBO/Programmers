from itertools import permutations

def solution(expression):
    answer = []

    nums = []
    operands = ["X"]

    tmp_nums = ""
    for e in expression:
        if not e.isdigit():
            nums.append(int(tmp_nums))
            tmp_nums = ""
            operands.append(e)
        else:
            tmp_nums += e
    nums.append(int(tmp_nums))

    def operator(operand, a, b):
        if operand == "*":
            return a * b
        elif operand == "+":
            return a + b
        else:
            return a - b
    original_nums = nums
    original_operands = operands

    for lst in permutations(["*", "-", "+"], 3):
        nums = original_nums
        operands= original_operands
        for l in lst:
            tmp_nums = []
            tmp_operands = []
            for i in range(len(nums)):
                if operands[i] == l:
                    tmp_nums.append(operator(l, tmp_nums.pop(), nums[i]))
                else:
                    tmp_operands.append(operands[i])
                    tmp_nums.append(nums[i])
            nums = tmp_nums
            operands = tmp_operands



        answer.append(abs(nums[0]))


    return max(answer)