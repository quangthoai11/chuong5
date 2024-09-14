# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:19 2024

@author: Admin
"""

def liet_ke_nghiem_toi_uu(a, b, c, n):
  """Liệt kê tất cả các bộ nghiệm nguyên dương của phương trình ax + by + cz = n.

  Args:
    a, b, c: Hệ số của x, y, z.
    n: Giá trị tự do.
  """

  for x in range(1, n // a + 1):
    for y in range(1, (n - a*x) // b + 1):
      z = n - a*x - b*y
      if z % c == 0 and z > 0:
        print(f"Nghiệm: (x, y, z) = ({x}, {y}, {z // c})")

# Thay đổi các hệ số và giá trị tự do ở đây
a = 2
b = 7
c = 9
n = 979

liet_ke_nghiem_toi_uu(a, b, c, n)