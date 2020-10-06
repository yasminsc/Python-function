from dot import Dot
from dot_on_line import is_dot_on_line

def print_result(a, b, c):
    if is_dot_on_line(a, b, c) == 1:
        print("dot c (" + str(c.x1) + "," + str(c.x2) + ") is on the line a-b: a(" + str(a.x1) + "," + str(a.x2) + ") , b(" + str(b.x1) + "," + str(b.x2) + ")")
    else:
        print("dot c (" + str(c.x1) + "," + str(c.x2) + ") is not on the line a-b a(" + str(a.x1) + "," + str(a.x2) + ") , b(" + str(b.x1) + "," + str(b.x2) + ")")

a = Dot(1, 9)
b = Dot(-1, 1)
c = Dot(0, 5)
d = Dot(0, 5)
e = Dot(1, 2)
f = Dot(3, -7)
g = Dot(1, 4)
h = Dot(1, 3)
i = Dot(-0.99999999, 1)
i2 = Dot(-0.999999999, 1)
print_result(a, b, c)
print_result(a, i, c)
print_result(a, i2, c)
print_result(a, d, c)
print_result(d, b, c)
print_result(g, e, h)
print_result(g, e, d)