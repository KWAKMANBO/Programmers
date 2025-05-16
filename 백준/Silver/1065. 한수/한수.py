import sys

input = sys.stdin.readline

N = input()

# 1~99는 무조건 한수
intN = int(N)
if intN < 100:
    print(intN)
else:
    answer = 99
    for i in range(100, intN+1):
        nums = [int(s) for s in str(i)]
        ratio = nums[1] - nums[0]
        flag = True
        for j in range(1, len(nums) - 1):
            if ratio != nums[j + 1] - nums[j]:
                flag = False
                break

        if flag:
            answer += 1
    print(answer)
