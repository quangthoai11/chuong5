# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:58 2024

@author: Admin
"""

def liet_ke_nghiem_toi_uu_tong_lon_nhat(a, b, c, n):
  """Liệt kê bộ nghiệm nguyên dương của phương trình ax + by + cz = n có tổng x+y+z lớn nhất.

  Args:
    a, b, c: Hệ số của x, y, z.
    n: Giá trị tự do.
  """

  max_sum = 0
  max_solution = (0, 0, 0)

  for x in range(1, n // a + 1):
    for y in range(1, (n - a*x) // b + 1):
      z = n - a*x - b*y
      if z % c == 0 and z > 0:
        current_sum = x + y + z
        if current_sum > max_sum:
          max_sum = current_sum
          max_solution = (x, y, z)

  print(f"Nghiệm có tổng lớn nhất: {max_solution}")

# Thay đổi các hệ số và giá trị tự do ở đây
a = 2
b = 7
c = 9
n = 979

liet_ke_nghiem_toi_uu_tong_lon_nhat(a, b, c, n)