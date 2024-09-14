# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:21:12 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S = sum(range(1, n + 1))
    print(f"Tổng S từ 1 đến {n} là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")
