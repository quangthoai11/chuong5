# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:00:03 2024

@author: PC
"""

nhan_vien = [
    {"loai": "NVVanPhong", "ma_nv": "NV001", "ho_ten": "Nguyen Van A", "luong_co_ban": 5000000, "luong_hang_thang": 6000000, "so_ngay": 22},
    {"loai": "NVVanPhong", "ma_nv": "NV002", "ho_ten": "Tran Thi B", "luong_co_ban": 5500000, "luong_hang_thang": 6500000, "so_ngay": 20},
    {"loai": "NVVanPhong", "ma_nv": "NV003", "ho_ten": "Le Thi C", "luong_co_ban": 6000000, "luong_hang_thang": 7000000, "so_ngay": 21},
    {"loai": "NVVanPhong", "ma_nv": "NV004", "ho_ten": "Hoang Van D", "luong_co_ban": 5200000, "luong_hang_thang": 6200000, "so_ngay": 23},
    {"loai": "NVVanPhong", "ma_nv": "NV005", "ho_ten": "Nguyen Thi E", "luong_co_ban": 5300000, "luong_hang_thang": 6300000, "so_ngay": 25},
    {"loai": "NVBanHang", "ma_nv": "NV006", "ho_ten": "Mai Van F", "luong_co_ban": 5000000, "luong_hang_thang": 7000000, "so_san_pham": 50},
    {"loai": "NVBanHang", "ma_nv": "NV007", "ho_ten": "Vu Thi G", "luong_co_ban": 5500000, "luong_hang_thang": 7500000, "so_san_pham": 55},
    {"loai": "NVBanHang", "ma_nv": "NV008", "ho_ten": "Do Thi H", "luong_co_ban": 6000000, "luong_hang_thang": 8000000, "so_san_pham": 60},
    {"loai": "NVBanHang", "ma_nv": "NV009", "ho_ten": "Nguyen Van I", "luong_co_ban": 5200000, "luong_hang_thang": 7200000, "so_san_pham": 45},
    {"loai": "NVBanHang", "ma_nv": "NV010", "ho_ten": "Tran Van J", "luong_co_ban": 5300000, "luong_hang_thang": 7300000, "so_san_pham": 48},
]
for nv in nhan_vien:
    if nv["loai"] == "NVVanPhong":
        print(f"Nhân viên văn phòng: Mã NV: {nv['ma_nv']}, Họ và tên: {nv['ho_ten']}, Lương cơ bản: {nv['luong_co_ban']}, Lương hàng tháng: {nv['luong_hang_thang']}, Số ngày: {nv['so_ngay']}")
    elif nv["loai"] == "NVBanHang":
        print(f"Nhân viên bán hàng: Mã NV: {nv['ma_nv']}, Họ và tên: {nv['ho_ten']}, Lương cơ bản: {nv['luong_co_ban']}, Lương hàng tháng: {nv['luong_hang_thang']}, Số sản phẩm: {nv['so_san_pham']}")
