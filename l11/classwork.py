from datetime import date
import json
from functools import reduce

from textwrap import indent

# obj = [1,2,3,4]
obj = [
{
    "ism": "Otabek",
    "kursi": 2,
    "yoshi": 23,
    "sana": date(day=23,month=5, year=2000).strftime("%d.%m.%Y"),
    "True": True,
    "None": None,
    "list": [3,4,5],
    "tuple": (4,5,6)
}
]
#

with open("data.txt", "w") as file:
    json.dump(obj, file,indent=4)

with open("data.txt", "r") as file:
    data = json.load(file)
print(data)
2
age = 0
with open("data.json", "r") as f:
    data = json.load(f)
a = [age['age'] for age in data['users']]
print(sum(a))

3

obj = {
  "products": [
    {"name": "Olma", "price": 5000},
    {"name": "Shaftoli", "price": 7000}
  ]
}
with open("products.json", "w") as f:
    json.dump(obj, f)
with open("products.json", "r") as f:
    data = json.load(f)
a = [name['name'] for name in data['products']]
b = [price['price']for price in data['products']]

4

with open("ppl.json", "r") as f:
    data = json.load(f)
lst = data['people']
p = reduce (lambda x, y: x if x['age']>y['age'] else y, lst)

print(p['name'])

5

with open("contacts.json", "r") as f:
    data = json.load(f)
# lst = []
a = [phone['phone'] for phone in data['contacts']]
print(a)


6

with open("students.json", "r") as f:
    data = json.load(f)
for a in data['students']:
    print(a['name'], sum(a['grades'])/len(a['grades']))


7

with open("users.json", "r") as f:
    data = json.load(f)
a = [a['name'] for a in data['users'] if a['role']=="admin"]
print(a)

#8

with open("categories.json", "r") as f:
    data = json.load(f)
n = None
rmax = 0
for item in data['categories'].items():
    if len(item[1])>rmax:
        rmax = len(item[1])
        n = item[0]
print(n)

# 9
with open("births.json", "r") as f:
    data = json.load(f)
a = [item for item in data['people']]
rslt = list()
for i in a:
    if i['birth_year']>1990:
        rslt.append(i['name'])
print(rslt)

#10

with open("departments.json", "r") as f:
    data = json.load(f)
for key, item in data['departments'].items():
    # a = item.keys()
    print(f"{key}:{len(item)}")

#11

with open ("orders.json", "r") as f:
    data = json.load(f)
temp = {}
for item in data["orders"]:
    name = item["customer"]
    amt = item["amount"]
    if name in temp:
        temp[name] +=amt
    else:
        temp[name] = amt
print(temp)

#12

with open ("courses.json", "r") as f:
    data = json.load(f)

for key, value in data['courses'].items():
    # print(f"{key}, {(value[0]['grade']+value[1]['grade'])/2}")
    total = sum(val['grade'] for val in value)
    print(f"{key}: {total/len(value)}")

#13

with open ("products.json", "r") as f:
    data = json.load(f)
max_product = max(data['products'], key=lambda x: x['price'])
print(f"{max_product['name']}: {max_product['price']}")

14

with open ("sales.json", "r") as f:
    data = json.load(f)

temp = {}
for item in data['sales']:
    n = item['month']
    a = item['amount']
    if n in temp:
        temp[n]+=a
    else:
        temp[n] = a
print(temp)

#15

with open("social_users.json", "r") as f:
    data = json.load(f)
rslt = []
for user in data['users']:
    if len(user['social'])>1:
        rslt.append(user['name'])

print(rslt)

#v4 4-ex

with open("weather.json", "r") as f:
    data = json.load(f)
max_temp = data[0]['temperature']
h_city = None
average = 0
for item in data:
    print(f"{item['city']}: {item['temperature']}")
    # hottest = (item['temperature'])
    # print(hottest)
    if item['temperature']>max_temp:
        max_temp = item['temperature']
        h_city = item['city']
    average+=item['temperature']
print("Eng issiq shahar: ", h_city, max_temp)
print("O'rtacha harorat: ", average/len(data))

#v3 4-ex
#
with open ("temps.json", "r") as f:
    data = json.load(f)
hottest = None
temp = {}
result = {}
# print(data)
for key, item in data.items():
    average = sum(item)/len(item)
    # print(key, average)
    temp[key] = average
    result['average'] = temp
# print(temp)
hottest = max(temp, key = temp.get)
coldest = min(temp, key = temp.get)
# print(hottest)
# print(coldest)
result['hottest'] = hottest
result['coldest'] = coldest
print(result)