T = int(input())

for test_case in range(1, T + 1):
    string = input()

    year = string[0:4]
    month = string[4:6]
    day = string[6:]

    if int(month) > 12 or int(month) < 1:
        print(f"#{test_case} -1")
    else:
        if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(
                month) == 10 or int(month) == 12:
            if int(day) > 31 or int(day) < 1:
                print(f"#{test_case} -1")
            else:
                print(f"#{test_case} {year}/{month}/{day}")
        elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
            if int(day) > 30 or int(day) < 1:
                print(f"#{test_case} -1")
            else:
                print(f"#{test_case} {year}/{month}/{day}")
        else:
            if int(day) < 1 or int(day) > 28:
                print(f"#{test_case} -1")
            else:
                print(f"#{test_case} {year}/{month}/{day}")
