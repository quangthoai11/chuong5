# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:56:51 2024

@author: PC
"""

import random
n = int(input("Nhập số lượng vé số: "))
ve_mua = [list(map(int, input(f"Nhập 6 số cho vé số {i+1} (cách nhau bởi dấu '-'): ").split('-'))) for i in range(n)]
day_so_trung_thuong = sorted(random.sample(range(1, 46), 6))
print(f"Dãy số trúng thưởng: {day_so_trung_thuong}")
tong_tien = 0
for ve in ve_mua:
    trung_so = len([num for num in ve if num in day_so_trung_thuong])
    if trung_so == 6:
        tong_tien += 10_000_000_000
    elif trung_so == 5:
        tong_tien += 10_000_000
    elif trung_so == 4:
        tong_tien += 300_000
    elif trung_so == 3:
        tong_tien += 30_000
print(f"Tổng số tiền người chơi nhận được: {tong_tien} đ")
