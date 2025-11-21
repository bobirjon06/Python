# #3
# from random import randint
#
#
# def raqamgacha_yigindi(son:int)->int:
#     rsum = 0
#     for i in range(0, son+1):
#         rsum+=i
#     return rsum
#
# #4
#
# def rand_num(n:int)->int:
#     return randint(10**(n-1), 10**n-1)
#
# #5
#
# def fac(n:int)->list:
#     lst = list()
#     for i in range(2, n):
#         if n%i==0:
#             lst.append(i)
#     return lst
#
# #6
#
# def pos_lst(lst:list)->list:
#     lst.sort()
#     ir = 0
#     for i in range(0, len(lst)):
#         if lst[i] >=0:
#             ir = i
#             break
#     return lst[ir::]
#
# print(pos_lst([1, -1, 2, 9, -3, -11, 20, 5, -8, 4]))
#
# #7
#
#
# #9
#
# def ret_max(lst:list)->int:
#     return max(lst)
#
# #10
#
# def rec(a:int, b:int)->tuple:
#     return (a+b)*2, a*2

lst = ["r>", "sdfs", "sdfsdf", "werwqrwr"]
# royxat = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# royxat.sort(key=lambda x: x[1])
# print(royxat)
lst.sort(key=lambda x: len(x))
print(lst)