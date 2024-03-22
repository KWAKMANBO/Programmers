def solution(array, commands):
    answer = []
    for i,j,k in commands:
        # i는 시작점
        # j는 종료점
        # k는 정렬 후 k번째 숫자
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
        
    return answer