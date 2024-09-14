# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:01:56 2024

@author: Admin
"""

def tim_nghiem_tong_nho_nhat(a, b, c, n):
  """Tìm bộ nghiệm nguyên dương của phương trình ax + by + cz = n có tổng x+y+z nhỏ nhất.

  Args:
    a, b, c: Hệ số của x, y, z.
    n: Giá trị tự do.
  """

  min_sum = float('inf')
  min_solution = None

  for x in range(1, n // a + 1):
    for y in range(1, (n - a*x) // b + 1):
      z = (n - a*x - b*y) // c
      if z > 0:
        current_sum = x + y + z
        if current_sum < min_sum:
          min_sum = current_sum
          min_solution = (x, y, z)
          # Cắt tỉa: Giảm giới hạn trên của y để loại bỏ các nghiệm có tổng lớn hơn
          y_max = (n - a*x - c*z) // b

  return min_solution

# Thay đổi các hệ số và giá trị tự do ở đây
a = 2
b = 7
c = 9
n = 979

result = tim_nghiem_tong_nho_nhat(a, b, c, n)
print(f"Nghiệm có tổng nhỏ nhất: {result}")