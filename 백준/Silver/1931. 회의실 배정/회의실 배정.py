import sys

n = int(input())

meeting_list = []

for _ in range(n):
    meeting_list.append(list(map(int, sys.stdin.readline().split())))

# meeting_list를 종료시간으로 정렬 후 종료시간이 같으면 시작 시간순으로 정렬
meeting_list.sort(key= lambda x : [x[1], x[0]])

answer = 0
end_time = 0
for s,e in meeting_list:
    if s >= end_time:
        answer +=1
        end_time = e

print(answer)