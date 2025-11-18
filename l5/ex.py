#1

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
a=3
b=9

for i in range(a, b):
    if i > 1:
        isPrime = True
        if i == 2:
            print(i)
        else:
            for j in range(2, i):
                if i%j==0:
                    isPrime = False
                    break
        if isPrime:
            print(i)


#2

n = int(input())
count = 0
while n%2==0:
    count += 1
    n = n/2
print(count)