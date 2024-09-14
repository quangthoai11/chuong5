# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:53:40 2024

@author: PC
"""

import string
id_user = input("Nhập ID User: ")
password = input("Nhập mật khẩu: ")
# Kiểm tra ID User
if not (6 <= len(id_user) <= 24):
    print("ID User phải có từ 6 đến 24 ký tự.")
elif any(char in "!@#$%^&*()-=+" for char in id_user):
    print("ID User không được chứa các ký tự đặc biệt: ! @ # $ % ^ & * ( ) - = +")
elif ' ' in id_user:
    print("ID User không được chứa khoảng trắng.")
else:
    # Kiểm tra Password
    if not (6 <= len(password) <= 24):
        print("Mật khẩu phải có từ 6 đến 24 ký tự.")
    elif not any(char.islower() for char in password):
        print("Mật khẩu phải chứa ít nhất 1 chữ cái ở dạng chữ thường (a-z).")
    elif not any(char.isdigit() for char in password):
        print("Mật khẩu phải chứa ít nhất 1 số (0-9).")
    elif not any(char.isupper() for char in password):
        print("Mật khẩu phải chứa ít nhất 1 chữ cái ở dạng chữ hoa (A-Z).")
    elif not any(char in "$#@" for char in password):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt trong [$ # @].")
    else:
        print("Đăng nhập thành công.")
