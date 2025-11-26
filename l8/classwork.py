import math
import random

# #1
# try:
#     n = int(input())
#     print(n)
# except ValueError:
#     print("Son kiriting!")
#
# #2
#
# a = int(input())
# b = int(input())
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas")
#
# #4
# lst = [1, 2, 3]
# index = 5
#
# try:
#     print(lst[index])
# except IndexError:
#     print("Out of range")
#
# #5
# try:
#     n = int(input())
#     print(math.ceil(n/3))
# except ValueError:
#     print("Son kiriting")
#
# lst = ["olma", "banan", "anor"]
# a = random.choice(lst)
# b = input()
# if a.lower()==b.lower():
#     print(a)
#     print("Found")
# else:
#     print(a)
#     print("No")

# r = "evermore"
# b = list(r)
# random.shuffle(b)
# print("".join(b))
# # simple_qr.py
# import qrcode
#
# def text_to_qr(text: str, filename: str = "qr.png", box_size: int = 10, border: int = 4,
#                error_correction=qrcode.constants.ERROR_CORRECT_M):
#     qr = qrcode.QRCode(
#         error_correction=error_correction,
#         box_size=box_size,
#         border=border,
#     )
#     qr.add_data(text)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(filename)
#     print(f"QR saved to: {filename}")
#
# if __name__ == "__main__":
#     txt = input("QR ga aylantirmoqchi bo'lgan matnni kiriting: ")
#     text_to_qr(txt, "my_qr.png")
