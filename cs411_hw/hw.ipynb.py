lst1 = [1,2,4,45,6,6,3]
lst2 = [1,2,4,5,6,2,45,5,6,7,845,1,3]
ans = set(lst1).intersection(set(lst2))
print(sorted(ans))