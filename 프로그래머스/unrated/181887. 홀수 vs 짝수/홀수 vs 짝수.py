def solution(num_list):
    even = num_list[0::2]
    odd = num_list[1::2]
    sum_even = sum(even)
    sum_odd = sum(odd)
    
    if sum_even > sum_odd:
        return sum_even
    else:
        return sum_odd
