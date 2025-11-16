# print("does it feel alright to not know me???")
#
# fruits = {"apple", "banana", "cherry", "apple"}
# print(type(fruits))
# fruits.update({"orange"})
# print(fruits)
#
# new_fruits = {"banana", "cherry", "orange", "mango", "pineapple"}
# print(new_fruits)
# # fruits.update(new_fruits)
# print(fruits)
# print(fruits.difference(new_fruits))
# print(fruits.intersection(new_fruits))
from itertools import count

#1
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print({n for n in set1 if n%2==0})
print(max(set1))
print(min(set1))
if 5 in set1:
    print(True)
else:
    print(False)

print({n for n in set1 if n>0})
print(len(set1))

#2
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
print(set1 == set2)

n = 20
set1.add(n)
print(set1)
print(min(set1))
set1.discard(min(set1))
print(set1)

lst = list(set1)
lst.sort()
print(lst)
print(set1.union(set2))
word = "champagne"
set1 = set(word)
print(set1)

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)