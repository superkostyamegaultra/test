import math

x = 10000
y = 1
a = 0
b = 0
c = 0

d = 0
while y <= 100:
    a = x / y
    a = math.floor(a)
    b = x - (y * a)
    b =abs(b)
    a += 1
    c = x - (y * a)
    c = abs(c)
    if b > c:
        print(y, a, d)

    else:
        a -= 1
        d = y*a
        print(y, a, d)
    y += 1


