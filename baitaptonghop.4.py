# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:28:47 2024

@author: Admin
"""

import random

def kiem_tra_ket_qua(nguoi_chon, may_chon):
    ket_qua = {
        ("Kéo", "Bao"): "thắng",
        ("Búa", "Kéo"): "thắng",
        ("Bao", "Búa"): "thắng",
        ("Kéo", "Kéo"): "hòa",
        ("Búa", "Búa"): "hòa",
        ("Bao", "Bao"): "hòa"
    }
    return ket_qua.get((nguoi_chon, may_chon), "thua")

def keo_bua_bao():
    lua_chon = ["Kéo", "Búa", "Bao"]

    while True:
        may_chon = random.choice(lua_chon)
        nguoi_chon = input("Bạn chọn gì? (Kéo/Búa/Bao): ").title()

        if nguoi_chon not in lua_chon:
            print("Lựa chọn không hợp lệ.")
            continue

        ket_qua = kiem_tra_ket_qua(nguoi_chon, may_chon)
        print(f"Bạn chọn {nguoi_chon}, máy chọn {may_chon}. Bạn {ket_qua}!")

        play_again = input("Chơi tiếp không? (có/không): ").lower()
        if play_again != "có":
            break

keo_bua_bao()