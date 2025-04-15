def solution(word):
    answer = 0
    nums = [781, 156, 31, 6, 1]
    word += (5 - len(word)) * '0'

    for i in range(5):
        if word[i] != '0':
            answer += 'AEIOU'.index(word[i]) * nums[i] + 1
        else:
            break

    return answer
