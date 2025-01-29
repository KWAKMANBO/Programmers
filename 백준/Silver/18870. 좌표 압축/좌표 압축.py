import sys

n = int(sys.stdin.readline())
original_lst = list((map(int, sys.stdin.readline().strip().split())))
sorted_lst = sorted(list(set(original_lst)))

result = {sorted_lst[i] : i for i in range(len(sorted_lst)) }

for i in original_lst:
    print(result[i], end =" ")