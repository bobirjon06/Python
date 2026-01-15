import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a[0])
# print(a[7:10])
# print(a*3)

b = np.array([3,5,7,3,2,4])
# mask = b>5
# print(b[mask])

c = np.array([12,4,7,15,3,9,20])
mask = c>10
# print(c[mask])
# fil = 5 <= c <= 15
# print(fil)

x = np.array([
    [10, 20, 30],
    [5,  15, 25],
    [0,  50, 100]
])
# print(x[1])
# print(x[:, 2])
#
# print(x.sum(axis=0))
# print(x.max(axis=1))

y = np.array([
    [2, 4, 6],
    [1, 3, 5]
])

add = np.array([10,20,30])
print(y+add)
m = np.array([1,2])
print(y*m[:, np.newaxis])