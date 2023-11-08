#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:51:16 2023

@author: paulin
"""

# def repeat_print(msg, n = 5):
#     while n > 0:
#         print(msg, end='')
#         n -=1
        
# repeat_print('a', 4)


# print(range(1,2,3,4,5,6,7,8,9,10))

# def s(x):
#     return x ** 2
# tot = 0
# for i in [1,3,5]:
#     tot += s(i)
# print(tot)

# import math

# count = 5
# n = 11
# while (count < n) :
#     print(count)
#     count = count + 3
    
    
#print(math.ceil((n-5)/3))

# import sys

# print(sys.path)

# import numpy as np
# from scipy.stats import norm
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(1, 1)


# mean, var, skew, kurt = norm.stats(moments='mvsk')

# x = np.linspace(norm.ppf(0.01),
#                 norm.ppf(0.99), 100)
# ax.plot(x, norm.pdf(x),
#        'r-', lw=5, alpha=0.6, label='norm pdf')

# rv = norm()
# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# vals = norm.ppf([0.001, 0.5, 0.999])
# np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))

# #r = norm.rvs(size=1000)

# r = norm.cdf(1900, loc = 1500, scale = 300)

# ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
# ax.set_xlim([x[0], x[-1]])
# ax.legend(loc='best', frameon=False)
# plt.show()

# import pdb; 

# pdb.set_trace()

import numpy as np

# print("option 1")
# print(np.random.choice(['a', 'b', 'c'], size = 3, replace=False))
# print("option 2")
# print(np.random.choice(['a', 'b', 'c', 'd', 'e'], size = 5, replace=True)[:3])
# print("option 3")
# print(np.random.choice(['a', 'b', 'c', 'd', 'e'], size = 5, replace=False)[:3])
# #print(np.random.choice(['a', 'b'], size = 3, replace=False))

def add_marker() :
    data=[]
    data.append("marker")
    return data

v1 = add_marker()
v2 = add_marker()
v3 = add_marker()

print(v1)
