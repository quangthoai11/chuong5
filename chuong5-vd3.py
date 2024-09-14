# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:43:26 2024

@author: Admin
"""

n = int(input("Nhập vào một số nguyên dương n: "))
dict = {i: i**3 for i in range(1, n+1)}
print(dict)