N = int(input())

lst = []
flag = False

for _ in range(N):
    univ = input()
    if univ == "korea":
        flag = True

    if univ == "yonsei" and not flag:
        print("Yonsei Won!")
    elif univ == "yonsei" and flag:
        print("Yonsei Lost...")

