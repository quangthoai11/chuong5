# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:01:56 2024

@author: Admin
"""

a, b, c, n = 2, 7, 9, 979

min_sum = float('inf')
solutions = []

for x in range(1, n // a + 1):
    for y in range(1, (n - a * x) // b + 1):
        if (n - a * x - b * y) % c == 0:
            z = (n - a * x - b * y) // c
            if z > 0:
                current_sum = x + y + z
                if current_sum < min_sum:
                    min_sum = current_sum
                    solutions = [(x, y, z)]
                elif current_sum == min_sum:
                    solutions += [(x, y, z)]
print("Các bộ nghiệm có tổng nhỏ nhất:")
for sol in solutions:
    print(sol)
