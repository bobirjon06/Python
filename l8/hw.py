import math
import random
import datetime
from datetime import timedelta
from random import randint
from time import strptime, strftime
import converter
import shapes

import requests

from converter import usd_to_uzs
from shapes import circle_area, rectangle_area


#1

lst = [1,2,3,4,5,6]
print(random.sample(lst, 3))

#2

a = 30
print(math.sin(math.radians(a)))

#3

print(strftime("%d-%B-%y, %A"))

#6

a = int(input())
n = randint(1, 100)
while a!=n:
    if a>n:
        print("Katta")
    else:
        print("Kichik")
    a = int(input())
else:
    print("Topdingiz!")

#7

n = int(input())
print(math.exp(n))

#8
a = "2025-08-16 10:00"
b = "2025-08-16 12:45"
f = "%Y-%m-%d %H:%M"
a_d = datetime.datetime.strptime(a, f)
b_d = datetime.datetime.strptime(b, f)
d = a_d-b_d
hr = d.seconds // 3600
m = (d.seconds // 60) % 60
print(f"{hr}:{m}")

# 9
url = "https://jsonplaceholder.typicode.com/todos"
r = requests.get(url)
data = r.json()
userid = [item ['userId'] for item in data]
print(userid)

# 10

n = 20
print(usd_to_uzs(20))


# 11

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url).json()
n = r[0]['name']
print(n)

# 12

r = 5
a = 4
b = 5
print(circle_area(r))
print(rectangle_area(a, b))
