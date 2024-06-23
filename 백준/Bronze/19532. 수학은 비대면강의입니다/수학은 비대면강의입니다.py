a, b, c, d, e, f = map(int, input().split())

x = ((c * e - b * f) // (a * e - b * d))
y = ((d * c - a * f) // (d * b - a * e))

print(x,y)
