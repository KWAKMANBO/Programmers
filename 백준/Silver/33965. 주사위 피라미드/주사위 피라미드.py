n = int(input())

p5 = 1
p4 = 2 * (n - 1) if n > 1 else 0
p3 = sum([i for i in range(1, n - 2 + 1)]) if n > 2 else 0
p2 = n - 1 if n > 1 else 0
p1 = 2 * sum([i for i in range(1, n - 2 + 1)]) if n > 2 else 0

d_min = [0, 1, 3, 6, 10, 15]
d_max = [0, 6, 11, 15, 18, 20]


min_answer = d_min[5] * p5 + d_min[4] * p4 + d_min[3] * p3 + d_min[2] * p2 + d_min[1] * p1
max_answer = d_max[5] * p5 + d_max[4] * p4 + d_max[3] * p3 + d_max[2] * p2 + d_max[1] * p1

print(min_answer + max_answer)
