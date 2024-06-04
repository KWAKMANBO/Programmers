import sys

string = sys.stdin.readline().rstrip()

i = 0
answer = 0

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    string = string.replace(i, " ")


print(len(string))