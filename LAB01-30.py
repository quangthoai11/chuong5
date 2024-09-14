# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:04:42 2024

@author: PC
"""

thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {thang} có 31 ngày.")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} có 30 ngày.")
elif thang == 2:
    print(f"Tháng 2 có {29 if nam_nhuan else 28} ngày.")
else:
    print("Tháng không hợp lệ!")