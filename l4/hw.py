#1

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
# print(set1.difference(set2))
sum1 = 0
sum2 = 0
for i in set1:
    if i in set.difference(set2):
        sum1 = sum1 + i
for i in set2:
    if i in set2.difference(set1):
        sum2 = sum2 + i
print(sum2-sum1)

#2

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

print((set1.intersection(set2)).difference(set3))

#3

set1={4,5,6,7,8,9}
set2={5,6,7,10,11}
sum1 = 0
sum2 = 0
for i in set1.union(set2):
    if i in set1.difference(set2) or i in set2.difference(set1):
        sum1 = sum1 + i
    elif i in set1.intersection(set2):
        sum2 = sum2 + i
# print(sum2, sum1)
print(sum1-sum2)

#4

set1={"Artel","Alif","Yandex", "Google", "Meta"}
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

print("Umumiy: ", set1.intersection(set2).intersection(set3))
print("Set1: ", set1.difference(set2.union(set3)))

#5

set1={2,3,4,5,6}
set2={4,5,6,7,8,9}
# sumR = 0
# setSum = set1.symmetric_difference(set2)
# for i in setSum:
#     sumR = sumR+i
# print(sumR)
print(sum(set1.symmetric_difference(set2)))

#6

set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}
set3 = set()
for i in set1.union(set2):
    if i>=60 and i in set1.intersection(set2):
        set3.add(i)
print(sum(set3)/len(set3))

#7

print(list(set(set1).intersection(set(set2))))

#8

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
set1 = set(nums1)
set2 = set(nums2)
list1 = list(set1-set2)
list2 = list(set2-set1)
ans = [list1, list2]
print(ans)

#9

nums = [1,2,2,3,1,4]
list1 = list()
list2 = list()
for num in nums:
    if num not in list1:
        list1.append(num)
        count = 0
        for r in nums:
            if r==num:
                count += 1
        list2.append(count)
max_fr = 0
for i in list2:
    if i>max_fr:
        max_fr = i
total = 0

for i in list2:
    if i==max_fr:
        total = total + i
print(total)

#10

list1 = [1, 2, 4, 5, 3, 2, 23, 34, 4, 20, 5, 7, 22, 1, 6]
set1 = set(list1)
list1 = list(set1)
print(list1)

#11

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

print(set1-set2)