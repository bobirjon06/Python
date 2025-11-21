#13

n = int(input())
a = 3
count = 0
while a<=n:
    a = a*3
    count +=1
print(count)

#14

n = int(input())
rmax = n%10
a = 0
while n!=0:
    a = n%10
    if a>rmax:
        rmax = a
    n/=10
print(int(rmax))

#19

n = int(input())
count = 0
while n%2!=1:
    n/=2
    count+=1
print(count)

#21

a = int(input())
b = int(input())


for i in range(a, b+1):
    isPrime = True
    if i>=2:
        isPrime = True
        for j in range(2, i):
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            print(i)