import json

with open("menu.json", "r") as f:
    data = json.load(f)
# print(data)
def apply_discount(food_name, discount_percent):
    # with open("menu.json", "w") as f1:
        for item in data:
            if item['name'].lower() == food_name.lower():
                nw = {'discount':1}
                item['price'] = item['price']*(1-discount_percent/100)
            else:
                nw = {'discount':0}
            item.update(nw)

        with open("menu.json", "w") as f1:
            json.dump(data, f1, indent=4)
        # print(data)
def add_new_food(food_name, price):
    temp = dict()
    temp['name'] = food_name
    temp['price'] = price
    temp['discount'] = 0
    data.append(temp)
    # print(data)
    with open("menu.json", "w") as f2:
        json.dump(data, f2, indent=4)

def change_food_price(food_name, new_price):
    for item in data:
        if item['name']==food_name:
            item['price'] = new_price
    with open("menu.json", "w") as f:
        json.dump(data, f, indent=4)
def get_most_expensive_food():
    rmax = dict()
    maxprice = 0
    for item in data:
        if item['price']>maxprice:
            maxprice = item['price']
            rmax = item
    return rmax['name'], rmax['price']
print("Barcha taomlar: ")
for i in data:
    print(i['name'])
c = input("Taom nomini kiriting: ")
for i in data:
    # print(i['name'])
    if i['name'].lower()==c.lower():
        print(f"{i['name']:_^5} narxi: {i['price']:_^5}")
        break
else:
    print("Bunday taom mavjud emas!")
n = input("Chegirma uchun taom nomini kiriting: ")
d = int(input("Chegirma foizini kiriting: "))
apply_discount(n, d)

print("Taomlar soni: ", len(data))

print("Narxi 30,000 dan past taomlar: ")
found = False
for i in data:
    if i['price']<=30000:
        print(f"- {i['name']:_^5} - {i['price']:_^5}")
        found = True
if not found:
    print("Topilmadi!")

f_n = input("Yangi taom nomini kiriting: ")
p_n = int(input("Narxini kiriting: "))
add_new_food(f_n, p_n)

change_food_price("Pepperoni", 55000)
print("Taom narxi o'zgaritrildi")
print("Eng qimmat taom", get_most_expensive_food())