#7

def kabisa_yilimi(yil):
    if yil%100!=0 and yil%4==0 or yil%400==0:
        return True
    # else:
    #     return False

def oyda_kun(yil, oy):
    lst1 = [1, 3, 5, 7, 8, 10, 12]
    lst2 = [4, 6, 9, 11]
    if oy in lst1:
        return 31
    elif oy in lst2:
        return 30
    elif kabisa_yilimi(yil):
        return 29
    else:
        return 28

def yilda_kun(yil, oy, kun):
    days = kun
    for i in range(1, oy):
        days+=oyda_kun(yil, i)
    return days


test_malumotlari = [1900, 2000, 2016, 1987]
test_natijalari = [False, True, True, False]

for i in range(len(test_malumotlari)):
    yil = test_malumotlari[i]
    javob = test_natijalari[i]
    if kabisa_yilimi(yil) == javob:
        print("To'g'ri")



yil = 2007
oy = 2
print(oyda_kun(yil, oy))

print(yilda_kun(yil, 5, 20))

#qiyin
#1
def toDict(a):
    result = {}
    for i in a:
        key = i[0]
        val = i[1]
        result[key] = val
    return result

lst1 = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"],
]
print(toDict(lst1))

#2

def sortit(lst):
    odd = list()
    even = list()
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort(reverse=True)
    odd.sort(reverse=False)
    rslt = list()
    for i in range(len(lst)//2):
        rslt.append(odd[i])
        rslt.append(even[i])
    return rslt


lst = [1,2,3,4,5,6,7,8,9,10]
print(sortit(lst))

#3

def afunc(lst):
    result = []
    for i in lst:
        if i["age"]>18 and i["cars"] >1:
            result.append(i)
    return result

lst = [
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]

print(afunc(lst))


#rec
#3
def ev(n):
    if n<=0:
        return
    if n%2==0:
        print(n, end="")
    ev(n-1)

print(ev(10))

#4

def rev(n):
    if n ==0:
        return
    print(n%10, end=" ")
    rev(n//10)
rev(20200705)

#lambda

#1

is_an = lambda s1, s2:sorted(s1)==sorted(s2)
print(is_an("hello", "ohell"))
#2
on_dig = lambda s:[char for char in s if char.isdigit()]

print(on_dig("hellothere23431"))
#3

leap = lambda x: x%4==0 and x%100!=0 or x%400==0

print(leap(2023))

#4
s = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_subjects = sorted(s, key=lambda x: x[1])
print(sorted_subjects)

#5

a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sr = sorted(a, key=lambda x: x['model'])
print(sr)

#6

lst1 = [1, 2, 3, 5, 7, 8, 9, 10]
lst2 = [1, 2, 4, 8, 9]

inter = lambda x, a: sorted(list(set(lst1).intersection(set(lst2))))
print(inter(lst1, lst2))