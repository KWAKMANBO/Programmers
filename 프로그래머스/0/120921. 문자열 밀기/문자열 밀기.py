def solution(A, B):
    if A == B:
        return 0
    
    answer = 0
    original = A
    A = A[-1] + A[:len(A)-1]
    shift = 1
    while A != original:
        if A == B:
            return shift
        else:
            A = A[-1] + A[:len(A)-1]
            shift += 1
    
    return -1