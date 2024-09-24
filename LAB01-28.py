# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:37:04 2024

@author: PC
"""

N = int(input("Nhập vào một số nguyên dương N: "))
while N <= 0:
    N = int(input("Nhập vào một số nguyên dương N: "))
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
