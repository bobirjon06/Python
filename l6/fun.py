# import time
# import random
# import string
# import winsound
# target = "champagne"
#
# # tweak these to taste
# scramble_frames = 200      # how many times each letter glitches
# fast = 0.001               # speed of glitch frames
# hold = 0.0005               # small pause when the real letter locks in
#
# revealed = ""
#
# for real_char in target:
#     for _ in range(scramble_frames):
#         fake_char = random.choice(string.ascii_letters + string.digits + "!@#$%^&*()")
#         print("\r" + revealed + fake_char, end="", flush=True)
#         time.sleep(fast)
#
#     revealed += real_char
#     print("\r" + revealed, end="", flush=True)
#     winsound.Beep(1500, 20)
#     time.sleep(hold)
#
# print()
import tkinter as tk

root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="Hello!", font=("Arial", 24))
label.pack()

root.mainloop()
