import random
import numpy as np

def damage(a, b):
    x = 0
    for i in range(a):
        x += random.randint(1, b)
    print('造成' + str(x) + '点伤害')
    return

xx = np.loadtxt('magic.txt', dtype=np.str, delimiter=',')

while True:
    skill = int(input('魔法序号')) - 1
    skilllv = int(input('魔法等级'))
    a = int(xx[4 * skill + skilllv][2])
    b = int(xx[4 * skill + skilllv][3])
    
    damage(a, b)
