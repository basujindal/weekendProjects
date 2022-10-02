# This code will take the Bot to the center of the
# maze and back to the starting w/o further exploration.
# The code is written assuming that the bot has 3 sensors to sense the walls
# Code is for a 16x16 maze which is an international standard size.



import numpy as np

size = 16
a = np.zeros([size, size])
w = np.ones([4, size, size], dtype=int)
p_x, p_y = size-1, 0

f_sen, r_sen, b_sen, l_sen = 0, 1, 2, 3
orient = 0


def update_ori():
    # 0, 1, 2, 3 means forward, right, left, backward orientation
    global f_sen, r_sen, l_sen, b_sen
    if orient == 0:
        f_sen, r_sen, b_sen, l_sen = 0, 1, 2, 3
    if orient == 1:
        f_sen, r_sen, b_sen, l_sen = 1, 2, 3, 0
    if orient == 2:
        f_sen, r_sen, b_sen, l_sen = 2, 3, 0, 1
    if orient == 3:
        f_sen, r_sen, b_sen, l_sen = 3, 0, 1, 2


def init_a():
    for i in range(size):
        for j in range(size):
            a[i][j] = 300
    a[8][8] = 0
    a[7][8] = 0
    a[8][7] = 0
    a[7][7] = 0


def init_w():
    j = 0
    for i in range(size):
        w[3][i][j] = False
    j = size - 1
    for i in range(size):
        w[1][i][j] = False

    i = 0
    for j in range(size):
        w[0][i][j] = False
    i = size - 1
    for j in range(size):
        w[2][i][j] = False


def check():
    d = 0
    for i in range(size):
        for j in range(size):
            if a[i][j] == 300:
                d += 1
    if d == 0:
        return False
    else:
        return True


def fill_n(n):
    for i in range(size):
        for j in range(size):
            if a[i][j] == n:
                fill(i, j)

    if check():
        fill_n(n + 1)


def fill(i, j):

    if w[2][i][j]:
        if a[i + 1][j] > a[i][j]:
            a[i + 1][j] = a[i][j] + 1

    if w[1][i][j]:
        if a[i][j + 1] > a[i][j]:
            a[i][j + 1] = a[i][j] + 1

    if w[0][i][j]:
        if a[i - 1][j] > a[i][j]:
            a[i - 1][j] = a[i][j] + 1

    if w[3][i][j]:
        if a[i][j - 1] > a[i][j]:
            a[i][j - 1] = a[i][j] + 1


def move_for(i, j):
    global p_x, p_y, orient
    var1, var2, var3, var4 = 300, 300, 300, 300

    if w[2][i][j]:
        if a[i + 1][j] < a[i][j]:
            var1 = a[i + 1][j]

    if w[1][i][j]:
        if a[i][j + 1] < a[i][j]:
            var4 = a[i][j + 1]

    if w[0][i][j]:
        if a[i - 1][j] < a[i][j]:
            var3 = a[i - 1][j]

    if w[3][i][j]:
        if a[i][j - 1] < a[i][j]:
            var2 = a[i][j - 1]

    min_val = min(var1, var2, var3, var4)

    if min_val != 300:
        if min_val == var3:
            p_x -= 1
            orient = 0  # FORWARD
            print('for')

        elif min_val == var4:
            p_y += 1
            orient = 1
            update_ori()  # RIGHT
            print('right')

        elif min_val == var2:
            p_y -= 1
            orient = 3
            update_ori()  # LEFT
            print('left')

        elif min_val == var1:
            p_x += 1
            orient = 2
            update_ori()  # BACK
            print('back')

    else:
        p_x += 1
        print('back')


def make_wall():

    x, y, z = [int(x) for x in input("Enter wall sen_above, sen_right, sen_left: ").split()]
    # x, y, z are inputs from sen_above, sen_right, sen_left
    # if no wall, input 0, if wall, input 1 or any number except 0

    if x != 0:

        if orient == 0:
            w[f_sen][p_x][p_y] = False
            w[b_sen][p_x - 1][p_y] = False

        if orient == 1:
            w[f_sen][p_x][p_y] = False
            w[b_sen][p_x][p_y + 1] = False

        if orient == 2:
            w[f_sen][p_x][p_y] = False
            w[b_sen][p_x + 1][p_y] = False

        if orient == 3:
            w[f_sen][p_x][p_y] = False
            w[b_sen][p_x][p_y - 1] = False

    if y != 0:

        if orient == 0:
            w[r_sen][p_x][p_y] = False
            w[l_sen][p_x][p_y + 1] = False

        if orient == 1:
            w[r_sen][p_x][p_y] = False
            w[l_sen][p_x + 1][p_y] = False

        if orient == 2:
            w[r_sen][p_x][p_y] = False
            w[l_sen][p_x][p_y - 1] = False

        if orient == 3:
            w[r_sen][p_x][p_y] = False
            w[l_sen][p_x - 1][p_y] = False

    if z != 0:

        if orient == 0:
            print(p_x, p_y, 'yes')
            w[l_sen][p_x][p_y] = False
            w[r_sen][p_x][p_y - 1] = False
            print(p_y - 1)

        if orient == 1:
            w[l_sen][p_x][p_y] = False
            w[r_sen][p_x - 1][p_y] = False

        if orient == 2:
            w[l_sen][p_x][p_y] = False
            w[r_sen][p_x][p_y + 1] = False

        if orient == 3:
            w[l_sen][p_x][p_y] = False
            w[r_sen][p_x + 1][p_y] = False


def move_back(i, j):
    global p_x, p_y, orient
    var1, var2, var3, var4 = 0, 0, 0, 0

    if w[2][i][j]:
        if a[i + 1][j] > a[i][j]:
            var1 = a[i + 1][j]

    if w[1][i][j]:
        if a[i][j + 1] > a[i][j]:
            var4 = a[i][j + 1]

    if w[0][i][j]:
        if a[i - 1][j] > a[i][j]:
            var3 = a[i - 1][j]

    if w[3][i][j]:
        if a[i][j - 1] > a[i][j]:
            var2 = a[i][j - 1]

    max_val = max(var1, var2, var3, var4)

    if max_val != 0:
        if max_val == var3:
            p_x -= 1  # FORWARD
            orient = 0
            update_ori()
            print('for')

        elif max_val == var4:
            p_y += 1  # RIGHT
            orient = 1
            update_ori()
            print('right')

        elif max_val == var2:
            p_y -= 1  # LEFT
            orient = 3
            update_ori()
            print('left')

        elif max_val == var1:
            p_x += 1  # BACK
            orient = 2
            update_ori()
            print('back')

    else:
        p_x += 1
        orient = 2
        update_ori()
        print('back')


def check_reached(flag):
    if p_y == 0:
        if p_x == size - 1:
            flag = False
    return flag


init_a()
init_w()
while a[p_x, p_y] != 0:

    make_wall()
    print(w)
    init_a()
    fill_n(0)
    print(a)

    move_for(p_x, p_y)
    print(p_x, p_y)

print('REACHED CENTRE')

flag_back = True
while flag_back:

    make_wall()
    print(w)
    init_a()
    fill_n(0)
    print(a)
    move_back(p_x, p_y)
    print(p_x, p_y)
    flag_back = check_reached(flag_back)
print('REACHED START')
