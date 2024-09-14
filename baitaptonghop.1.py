# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:26:57 2024

@author: Admin
"""

def xuli_chuoi(str_input):
  """Hàm xử lý chuỗi, thực hiện các yêu ký tự đặc biệt, chữ cái, số"""

  # Tính độ dài chuỗi
  do_dai = len(str_input)
  print("Độ dài chuỗi:", do_dai)

  # Tập hợp các ký tự đặc biệt
  ky_tu_dac_biet = "!@#$%^&*()-+=./"

  # Khởi tạo các biến đếm
  dem_ky_tu_dac_biet = 0
  dem_chu_thuong = 0
  dem_chu_hoa = 0
  dem_so = 0

  # Duyệt từng ký tự trong chuỗi
  for ky_tu in str_input:
    if ky_tu in ky_tu_dac_biet:
      dem_ky_tu_dac_biet += 1
    elif ky_tu.isalpha():
      if ky_tu.islower():
        dem_chu_thuong += 1
      else:
        dem_chu_hoa += 1
    elif ky_tu.isdigit():
      dem_so += 1

  # In kết quả
  print("Số lượng ký tự đặc biệt:", dem_ky_tu_dac_biet)
  print("Số lượng chữ cái thường:", dem_chu_thuong)
  print("Số lượng chữ cái hoa:", dem_chu_hoa)
  print("Số lượng chữ số:", dem_so)

# Nhập chuỗi từ người dùng
str_input = input("Nhập chuỗi: ")

# Gọi hàm xử lý chuỗi
xuli_chuoi(str_input)