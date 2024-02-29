def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    
    plus = [i for i in numbers if i >= 0]
    minus = [i for i in numbers if i < 0]
    plus.sort()
    minus.sort()
    if len(minus) < 2:
        return plus[-1]*plus[-2]
    else: 
        return plus[-1]*plus[-2] if plus[-1]*plus[-2] >= minus[0]*minus[1] else minus[0]*minus[1]
        