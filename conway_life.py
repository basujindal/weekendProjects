import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
plt.style.use('dark_background')


# -------------------------------------------------------------
# RANDOM

size1 = 1000
size2 = 1000
prob = 0.5
life = np.random.choice([0,1],size=(size1, size2),p=[prob, 1-prob])

# ----------------------------------------

# GLIDER

# size1 = 30
# size2 = 30
# life = np.zeros((size1,size2), dtype=int)
# life[3,8] = 1
# life[4,8] = 1
# life[5,8] = 1
# life[5,7] = 1
# life[4,6] = 1

# -----------------------------------------

# BLOCK

# init = 20
# size1 = 30
# size2 = 30
# life = np.zeros((size1,size2), dtype=int)
# for i in range(init):
#     for j in range(init):
#         life[i,j] = 1

# ----------------------------------------

# PULSAR

# size1 = 15
# size2 = 15
# def init_universe_pulsar():
#     grid = np.zeros([15, 15])
#     line = np.zeros(15)
#     line[3:6] = 1
#     line[9:12] = 1
#     for ind in [1,6,8,13]:
#         grid[ind] = line
#         grid[:,ind] = line
#     return grid
# life = init_universe_pulsar()

# ----------------------------------------

# GLIDER_GUN

# size1 = 30
# size2 = 38
# def init_universe_glider_gun():
#     glider_gun = 38*'0' + 25*'0'+'1'+12*'0' + 23*'0'+'101'+12*'0' +\
#              13*'0'+'11'+6*'0'+'11'+12*'0'+'11'+'0' +\
#              12*'0'+'1'+3*'0'+'1'+4*'0'+'11'+12*'0'+'11'+'0' +\
#              '0'+'11'+8*'0'+'1'+5*'0'+'100011'+15*'0' +\
#              '0'+'11'+8*'0'+'1'+'000'+'1011'+4*'0'+'101'+12*'0' +\
#              11*'0'+'1000001'+7*'0'+'1'+12*'0' +\
#              12*'0'+'10001'+21*'0' + 13*'0'+'11'+23*'0' + 38*'0' +\
#              19*38*'0'
#     grid = np.array([float(g) for g in glider_gun]).reshape(30,38)
#     return grid
#
#
# life = init_universe_glider_gun()

# -------------------------------------------------------------------

next_life = np.zeros((size1,size2), dtype=int)
final = np.zeros((size1,size2), dtype=int)

span = 1500

for i in range(size1):
    for j in range(size2):
        final[i,j] = life[i,j]
final = np.expand_dims(final, axis=0)
counter = 0


def check_life(life1):
    global counter, final
    a = signal.convolve2d(life1,kernel,'same')
    for i in range(size1):
        for j in range(size2):
            if life1[i,j] == 1:
                if a[i,j] == 2:
                    next_life[i,j] = 1
                if a[i,j] == 3:
                    next_life[i,j] = 1
            if life1[i,j] == 0 and a[i,j] == 3:
                next_life[i,j] = 1
    if (life1 == next_life).all():
        print(a)

    final = np.concatenate((final,np.expand_dims(next_life,axis=0)))


for k in range(span):
    next_life = np.zeros((size1,size2),dtype=int)
    check_life(life)
    if (life == next_life).all():
        break
    for i in range(size1):
        for j in range(size2):
            life[i,j] = next_life[i,j]


c = final[0]
print(len(final))
im=plt.imshow(c)
for i in range(len(final)):
    im.set_data(final[i])
    plt.pause(0.1)
    # print('yes')
plt.show()
