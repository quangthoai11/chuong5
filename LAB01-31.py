# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:06:57 2024

@author: PC
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Tam giác vuông cân.")
        else:
            print("Tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông.")
    else:
        print("Tam giác thường.")
else:
    print("Không phải là tam giác.")
