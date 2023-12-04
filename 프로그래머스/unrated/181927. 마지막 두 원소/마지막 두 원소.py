# 만약 마지막 원소 > 그전 원소 --> 마지막 원소 - 그전 원소
# 마지막 뭔소 < 그전 원소 --> 마지막 원소 * 2
def solution(num_list):
    last = num_list[len(num_list)-1]
    beforeLast = num_list[len(num_list)-2] 
    if(last > beforeLast):
        num_list.append(last - beforeLast)
        return num_list
    else:
        num_list.append(last*2)
        return num_list