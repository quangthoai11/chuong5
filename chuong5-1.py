# -*- coding: utf-8 -*-
"""2

Spyder Editor

This is a temporary script file.
"""

n= int(input("Nhập số nguyên dương n: "))
if n>0:
    giai_thua= 1
    for i in range(1, n+1):
        giai_thua *= i
    print(f"Giai thừa của {n} là: {giai_thua}")
else:
    print("n không phải là số nguyên dương")
    