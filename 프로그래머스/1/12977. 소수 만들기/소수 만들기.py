def solution(nums):
    answer = 0
    primes = set(range(2, len(nums) * 1000 + 1))

    for i in range(2, len(nums) * 1000 + 1):
        if i in primes:
            primes -= set(range(2*i, len(nums) * 1000 + 1, i))
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] in primes:
                    # print(nums[i], nums[j], nums[k])
                    answer += 1

    return answer