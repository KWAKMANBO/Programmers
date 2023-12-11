#arr[i]가아니 i가 k의 배수 즉 index가 배수일 때 +1임

def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] +=1
    return arr