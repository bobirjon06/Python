import math
from functools import reduce
#1
lst = [4]

lst1 = filter(lambda x: x % 2 == 0, lst)
lst2 = map(lambda x: x**2, lst1)
print(reduce(lambda x,y: x+y, lst2))

#2
lst = ["olma", "banan", "anjir", "shaftoli"]

lst = (map(lambda x: len(x), lst))
# print(lst)
print(reduce(lambda x,y:x if x>y else y, lst))
#3
lst = [-2, 3, 4, -1, 2]

lst = filter(lambda x: x > 0, lst)
print(reduce(lambda x,y: x *y, lst))

#4

lst = ["a", "b", "a", "c", "b", "a"]
lst.sort()
print(reduce(lambda x, y:x if lst.count(x) else y, lst))

#5

lst = [10000, 20000, 5000]
lst = map(lambda x: x*1.12, lst)
print(reduce(lambda x, y: x+y, lst))

#6

lst = ["salom", "hi", "python"]
lst = map(lambda x: len(x), lst)
print(reduce(lambda x, y: x+y, lst))

#7
lst = [9, 2, 3, 5]

lst = filter(lambda x: x % 2 == 1, lst)
lst = map(lambda x: x**3, lst)
print(reduce(lambda x,y: x-y, lst))


#8

lst = [70, 80, 96, 100]

lst = list(map(lambda x:x*1.05 if x!=100 else x, lst))
print(reduce(lambda x,y:x+y,lst)/len(lst))

#9

lst = ["12", 7, "x", 5, "2"]
lst = list(filter(lambda x: type(x)==int, lst))
print(reduce(lambda x, y: x+y, lst))

#10

lst = ["web", "development", "with", "python"]
lst = list(map(lambda x:x.title(), lst))
print(reduce(lambda x,y: x+" "+y, lst))

#12

txt = "a1b20c3"
# lst = txt.split(txt)
# print(lst)
lst = list(txt)
# print(lst)
lst = list(filter(lambda x: x.isdigit(), lst))
# print(lst)
print(reduce(lambda x, y: int(x) + int(y), lst))

#13

lst = ["olma", "anjir", "uzum", "banan", "o‘rik", "shaftoli"]
a = "aeiuo"
lst = filter(lambda x: x[0] in a and len(x)>=5, lst )
lst = map(lambda x: 1, lst)
print(reduce(lambda x, y: x+y, lst))

#14

lst = [2, -1, 2, 3, 3, 0, 4]
lst = list(set(lst))
# print(lst)
lst = filter(lambda x: x > 0, lst)
# lst = map(lambda x: x ** 2, lst)
print(reduce(lambda x, y: x*y, lst))

#15

lst = ["data", "science", "ai"]
lst = map(lambda x: x[-1], lst)
print(reduce(lambda x, y: x+y, lst))

#16

lst = [1, 4, 7, 8, 10]
lst.sort()
n = len(lst)
med = lst[n//2]
print(reduce(lambda x, y: x if abs(x - med) < abs(y - med) else y, lst))


#17
def divisors(n):
    divisor = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
    return divisor

lst = [4, 6]

mapped = map(lambda x: sum(divisors(x)), lst)
total  = reduce(lambda x, y: x + y, mapped)

print(total)

#18

lst = ["a", "abbb", "cc", "ddd", "ee"]
lst = list(map(lambda x: len(x), lst))
rmax = int (reduce(lambda x, y: x if x > y else y, lst))
print(reduce(lambda x, y: x+(1 if y==rmax else 0), lst, 0))

#19

lst =[(80, 2), (90, 1), (100, 3)]

a = list(map(lambda x: x[0]*x[1], lst))
b = list(map(lambda x: x[1], lst))
print(reduce(lambda x, y: x + y, a)/reduce(lambda x, y: x + y, b))

#20

lst = [30, 50, 70, 90, 100]
lst = list(filter(lambda x: 50 <= x <= 90, lst))
print(reduce(lambda x, y: x+y, lst)/len(lst))