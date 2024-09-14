# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:49:38 2024

@author: Admin
"""

def tinh_tong(n):
  tong = 0
  for i in range(1, n+1):
    mau = 2 * i
    tong += 1 / mau
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)