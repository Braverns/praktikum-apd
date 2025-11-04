from math import sqrt, ceil, floor,sin
import pandas as pd
from random import randint, choice
import datetime
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


# num = int('100')
# name = str(100)
# data = list('abc')
# dict = dict(a=1, b=2)

# opsss = abs(-9)
# opss = max([1, 10, -1])
# ops = min([100, -1, -100])
# op = round(3.1428571428571,3)
# o = sum([100, -100, 1])

# ups = sqrt(16)
# up = ceil(3.2)
# u = floor(3.7)

# for i, v in enumerate(['a','b'], start = 1):
#     print(i, v) # 0 a , 1 b

# len([10, 20, 30]) # 3

# list(map(str, [1,2,3])) # ['1', '2', '3']

# sorted([3, 1, 2]) # [1, 2, 3]

# list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

# def gem(a):
#     b = ['gunting', 'batu', 'kertas']
#     choice(b)
#     if a == b:
#         print('Seri')
#     elif a == '1' and b == 'batu':
#         print('Kamu kalah dari batu')
#     elif a == '1' and b == 'kertas':
#         print('Kamu menang dari kertas')
#     elif a == '2' and b == 'batu':
#         print('Kamu menang dari batu')
#     elif a == '2' and b == 'gunting':
#         print('Kamu kalah dari gunting')
#     elif a == '3' and b == 'kertas':
#         print('Kamu kalah dari kertas')
#     else:
#         print('Kamu menang dari gunting')

# gem(input('1. Gunting \n2. Kertas \n3. Batu \nPilihan mu: '))
while True:
    xpoints = np.array([1, 1844])
    ypoints = np.array([1, randint(3,10), randint(3,10), randint(3,10), randint(7,20), randint(7,20), randint(7,25), randint(12,35), randint(12,35), randint(12,15), randint(9,15), randint(9,15), randint(9,15), randint(5,15), randint(5,10), randint(5,10), randint(2,8), randint(2,8), randint(2,8)])
    plt.plot(ypoints)
    plt.show()
    