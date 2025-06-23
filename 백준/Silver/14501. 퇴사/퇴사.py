import sys

input = sys.stdin.readline
# 일 수 입력
N = int(input())

# 정보 입력
works = [list(map(int, input().split())) for _ in range(N)]


# 재귀로 풀이
def recursive_solve(idx):
    # 매개변수로 입력된 idx가 N보다 크거나 같으면 0을 반환하고 종료
    if idx >= N:
        return 0

    result = 0
    # 추가할 업무의 소요일 수를 더했을때 N보다 작으면
    # 결과에 추가
    if idx + works[idx][0] <= N:
        # 재귀적으로 합쳐서 
        # 오늘 날짜를 선택하고 다음 그당므 날짜를 선택하는 경우 재귀적으로 계산하기 
        result = recursive_solve(idx + works[idx][0]) + works[idx][1]
    # 오늘 날짜를 선택하지 않고 다음 날짜부터 선택하는 경우 계산해서 비교하기  
    result = max(result, recursive_solve(idx + 1))

    return result


print(recursive_solve(0))
