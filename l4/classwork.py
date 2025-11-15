print("does it feel alright to not know me???")

fruits = {"apple", "banana", "cherry", "apple"}
print(type(fruits))
fruits.update({"orange"})
print(fruits)

new_fruits = {"banana", "cherry", "orange", "mango", "pineapple"}
print(new_fruits)
# fruits.update(new_fruits)
print(fruits)
print(fruits.difference(new_fruits))
print(fruits.intersection(new_fruits))