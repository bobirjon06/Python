# #3
# from random import randint
# lst = []
#
# for i in range(0,100):
#     n = randint(0, 1)
#     lst.append(n)
# maxlen = 0
# tempMax = 0
# for i in range(len(lst)):
#     if lst[i]==0:
#         tempMax +=1
#         if tempMax>maxlen:
#             maxlen=tempMax
#
#     else:
#         tempMax=0
# # if tempMax>maxlen:
# #     maxlen=tempMax
# print(lst)
# print(maxlen)


# #4
#
# lst = [1,1,2,3,4,3,0,0]
# result = []
# for i in lst:
#     if i not in result:
#         result.append(i)
# print(result)

# #18
#
# numbers = {3, 8, 15, 1, 10}
# print(max(numbers)-min(numbers))
#
# #19
#
# sample_set = {"y", "o", "b"}
# sample_list = ["B", "g", "r"]
# sample_list = set(sample_list)
# print(sample_set.union(sample_list))
# # print(result)

# #3
#
# r = "w3resource"
# lst = list(r)
# dict1 = {}
# for char in lst:
#     if char not in dict1:
#         dict1[char] = 1
#     else:
#         dict1[char]= dict1[char]+1
# print(dict1)


lst = ['S001', 'S002', 'S003', 'S004']
lst1 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
lst2 = [85, 98, 89, 92]


dict1 = dict()
dict2 = dict()
for i in range(len(lst)):
    dict2[lst1[i]] = lst2[i]
    dict1[lst[i]] = dict2
print(dict1)

# lst1 = [
#  {'S001': {'Adina Park': 85}},
#  {'S002': {'Leyton Marsh': 98}},
#  {'S003': {'Duncan Boyle': 89}},
#  {'S004': {'Saim Richards': 92}}
# ]