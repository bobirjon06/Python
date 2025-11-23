import random
from random import randint

# from random import randint
#
#
# #4
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# # n = int(input())
# n = 6
# for i in range(1, 6):
#     print(fib(i), end=" ")
#
# #10
#
# def three(n):
#     a = n
#     while a!=0:
#         if a%10==3:
#             return n
#         a = a//10
#     return 0
#
#
# for i in range(100, 1000):
#     if three(i)!=0:
#         print(three(i))


#2


#3



lst = list()

def maxnull(lst):
    maxcount = 0
    count = 0
    for i in range(len(lst)):
        if lst[i]==0:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
            count = 0
    return maxcount

for i in range(0, 100):
    lst.append(randint(0,1))
print(maxnull(lst))