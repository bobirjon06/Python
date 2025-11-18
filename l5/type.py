import time
import sys
lyrics = """
you booked the night train for a reason,
so you could sit there in this hurt.
bustling crowds or silent sleepers,
you're not sure which is worse.
because i dropped your hand while dancing,
left you out there standing.
crestfallen on the lantern,
champagne problems.
your mom's ring in your pocket,
my picture in your wallet.
your heart was glass i dropped it,
champagne problems.
you told your family for a reason,
you couldn't keep it in.
your sister's splashed out all the bottle,
and no one's celebrating...
dom perignon you brought it,
no crowd of friends applauded,
your hometown skeptics called it
champagne problems.
you had a speech you're speechless,
love slipped beyond your reaches,
you couldn't give a reason,
champagne problems...
your midas touch, on the chevy door,
november flush and your flannel cure,
this dorm was once a madhouse,
i made a joke \"well, it's made for me\"
how evergreen our group of friends
dont think we'll say that word again
and soon they all have the nerve to
deck the halls that we once walked through...
"""

for line in lyrics.split("\n"):
    for char in line:
        print("\033[94m" + char + "\033[0m", end="", flush=True)  # blue typing
        time.sleep(0.05)
    print()
    time.sleep(0.7)

# import time
# import random
# import string
#
# for _ in range(30):
#     line = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(60))
#     print(line)
#     time.sleep(0.5)
# print("ACCESS GRANTED")
## countdown
# import time
#
# for i in range(50, 0, -1):
#     print(f"\r{i} ", end="", flush=True)
#     # time.sleep(1)
#     time.sleep(0.05)
# print("\rGo!")
#bounce
# import time
#
# while True:
#     for i in range(4):
#         print("\rWaiting" + "." * i + " " * (3-i), end="", flush=True)
#         time.sleep(0.3)
#
