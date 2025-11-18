#1
dict1 = {'ism': 'Ali'}
dict2 = {'yosh': 20, 'kurs': 2}
dict1.update(dict2)
print(dict1)

#2

dict1 = {'A': 5, 'B': 15, 'C': 25}
sum1 = 0
for val in dict1.values():
    sum1 += val
print(sum1)

#3

dict1 = {'A': 5, 'B': 12, 'C': 9, 'D': 20}
dict2 = {}
for key, val in dict1.items():
    if val >=10:
        dict2.update({key:val})
print(dict2)

#4

dict1 = {'banana': 3, 'apple': 5, 'cherry': 2}
list1 = list(dict1.items())
list1.sort()
dict1 = list1
print(dict1)

#5

dict2 = {}
dict1 = {'ism': 'Ali', 'yosh': 20, 'kurs': 2, 'manzil': 'Toshkent'}
for k, v in dict1.items():
    if len(k)>3:
        dict2.update({k:v})
print(dict2)

#6

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#7

n = 6
dic = {}
for i in range(n+1):
    dic.update({i:i*i})
print(dic)

#8
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = {}
for key in d1.keys() | d2.keys():
    result[key] = d1.get(key,0) + d2.get(key,0)
print(result)

#9

n = int(input("nechta maxsulot?? "))
dic1 = {}
for i in range(n):
    name = input("name? ")
    price = float(input("price? "))
    dic1.update({name:price})
print(dic1)

#10

prices = {"Olma": 10000, "Nok": 15000, "Banan": 20000}

print(max(prices.values()))

#11
dic1 = {}
text = "salom dunyo salom python"
for word in text.split():
    if word not in dic1:
        dic1.update({word:1})
    else:
        dic1.update({word:dic1[word]+1})
print(dic1)

#12

d1 = {'Ali': 80, 'Vali': 95, 'Soli': 87}
print( max(d1, key=d1.get))

#13

d1 = {'ism': 'Ali', 'yosh': 20}
d2 = {}
for key, val in d1.items():
    d2.update({val:key})
print(d2)

#14

d1 = {
  "Ali": {"math": 80, "eng": 90, "prog": 85},
  "Vali": {"math": 70, "eng": 75, "prog": 80}
}

result = {}
for key, val in d1.items():
    result[key] = sum(val.values()) / len(val)

print(result)

#15

text = "Python Py"
dic = {}
for c in text:
    if c.isalpha() and c not in dic:
        dic.update({c:1})
    elif c.isalpha():
        dic.update({c:dic[c]+1})
print(dic)
