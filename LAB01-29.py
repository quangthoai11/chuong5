# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:58:45 2024

@author: PC
"""

N = int(input("Nhập vào một số nguyên dương N: "))
tong = 0
while N > 0:
    tong += N % 10
    N //= 10
print("Tổng các chữ số là:", tong)
