import sys

grade_list = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

sum_credit = 0
sum_grade = 0

for _ in range(50):
    try:
        subject, credit, grade = map(str, sys.stdin.readline().rstrip().split())
        credit = float(credit)
        if grade != "P":
            sum_credit += credit
            sum_grade += grade_list[grade] * credit
    except:
        break

print(sum_grade / sum_credit)
