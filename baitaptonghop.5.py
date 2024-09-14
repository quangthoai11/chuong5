# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:47:06 2024

@author: Admin
"""

import random

def keo_bua_bao_nhieu_nguoi(min_players=8, max_players=20):
    """
    Mô phỏng trò chơi Kéo-Búa-Bao với nhiều người chơi tự động.

    Args:
        min_players: Số lượng người chơi tối thiểu.
        max_players: Số lượng người chơi tối đa.
    """

    lua_chon = ["Kéo", "Búa", "Bao"]
    num_players = random.randint(min_players, max_players)

    # Tạo danh sách các người chơi và lựa chọn ngẫu nhiên
    players = [random.choice(lua_chon) for _ in range(num_players)]

    # Đếm số lượng người chơi chọn từng loại
    counts = {choice: players.count(choice) for choice in lua_chon}

    print(f"Có {num_players} người chơi tham gia.")
    print(f"Kết quả: {counts}")

    # Xác định người thắng (có thể có nhiều người thắng)
    max_count = max(counts.values())
    winners = [choice for choice, count in counts.items() if count == max_count]

    if len(winners) == 1:
        print(f"Người thắng là: {winners[0]}")
    else:
        print(f"Các người thắng là: {', '.join(winners)}")

# Chạy trò chơi
keo_bua_bao_nhieu_nguoi()