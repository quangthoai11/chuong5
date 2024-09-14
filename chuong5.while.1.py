# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:09:56 2024

@author: Admin
"""

while True:
  number = int(input("Nhập vào một số nguyên: "))
  if -99 <= number <= 99:
    print("Số bạn nhập đã hợp lệ.")
    break
  else:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")