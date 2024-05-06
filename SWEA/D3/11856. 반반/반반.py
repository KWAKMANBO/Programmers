t = int(input())

for test_case in range(1, t + 1):
    s = input()

    set_s = set(s)
    answer = "Yes"

    if len(set_s) == 2:
        for i in set_s:
            if s.count(i) != 2:
                answer = "No"
    else:
        answer = "No"

    print(f"#{test_case} {answer}")

