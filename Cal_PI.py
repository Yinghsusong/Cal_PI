# coding:utf-8
# Calculate the value of PI using the Monte Carlo method

import math
import random

import matplotlib.pyplot as plt
import numpy as np

# Calculate the root mean square of two numbers or radius
def cal_r(x,y):
    return math.sqrt(x*x+y*y)

# Draw a circle 
def draw_round(x):
    return math.sqrt(1-x*x)

# Randomly generate 10,000 points
x, y = [], []
for i in range(10000):
    x.append(random.random())
    y.append(random.random())

# Statistics point falling within the circle
num = 0
z = map(cal_r,x,y)
for r in z:
    if r <= 1:
        num = num + 1

# Calculate PI
pi = float(num/10000.0)*4

# Draw
r = np.linspace(0.0,1.0,200)
#########################################################
s = map(draw_round,r)
print(s) 
# <map object at 0x000002B531F3EE80>
s = list(s)

# Knowledge point: map function is not the same in py2 & py3
#########################################################

plt.plot(r,s,c = 'red', linewidth = '2')  

for x0,y0 in zip(x,y):
        if cal_r(x0,y0)<=1:
                plt.scatter(x0,y0,c='b')     
        else: 
                plt.scatter(x0,y0,c='g')     

# plt.scatter(x,y,c='b')   
plt.title(f'The Value of PI is {pi}')
plt.show()
