# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:10:26 2024

@author: Student
"""

import random
cau_1= random.randint(20,30)
cau_2= [random.uniform(18,99)**2 for i in range(cau_1)]
print(f"Số lượng phần tử trong danh sách: {cau_1}")
print("Danh sách các giá trị bình phương:")
for j in cau_2:
    print(f"{j:.2f}")
