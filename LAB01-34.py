# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:19:12 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương n: "))
if n <= 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố.")
            break
    else:
        print(f"{n} là số nguyên tố.")
