import math
import numpy as np
import matplotlib.pyplot as plt
z = 3 + 2j
a = 0
i = 0


def multi(num, c):
    global a,i
    a = num*num + c
    if a.real*a.real + a.imag*a.imag < 4:
        if i < 200:
            i += 1
            multi(a,c)
    return i


# print(multi(0, 2 + 2j))

pi = math.pi
r = 0
while r < 5:

    r += 0.1
    print(r)
    t = -2*pi
    while t < 2*pi:
        i = 0
        t += 0.1
        x = r * math.sin(t)
        y = r * math.cos(t)
        if multi(0,complex(x,y)) == 200:
            plt.scatter(x,y, s = 0.1)
            plt.savefig("foo.png")

plt.show()


