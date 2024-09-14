# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:32:00 2024

@author: Admin
"""

while True:
  try:
    number = float(input("Nhập vào một số thực: "))
    if number.is_integer():
      print("Vui lòng nhập số thực, không phải số nguyên.")
    elif -89.9 <= number <= 88.8:
      print("Số bạn nhập đã hợp lệ.")
      break
    else:
      print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")