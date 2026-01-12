# from functools import reduce
#
#
# def numof(nums):
#     lst = list(filter(lambda x: x if x%2==1 and nums.count(x)>1 else None, nums))
#     return len(set(lst))
# print(numof(
# [1,2,3,3,5,5,5,6]))
#
# def compress(text):
#     # text = text.split()
#     rslt = []
#     count = 1
#     for i in range(1, len(text)):
#         if text[i]==text[i-1]:
#             count+=1
#         else:
#             rslt.append((text[i-1], count))
#             count = 1
#     rslt.append((text[-1], count))
#     return rslt
# print(compress("aaabbcaaa"))
#
# def order_det(orders):
#     paid = list(filter(lambda x: x if x['status']=='paid'else None, orders))
#     return {
#   "total": len(orders),
#   "paid_count": len(paid),
#   "paid_sum": sum(list(map(lambda x: x['price'], paid))),
#   "unique_prices": len(set(list(map(lambda x:x['price'], orders))))
# }
# orders = [
#     {"id":1, "price":120, "status":"paid"},
#     {"id":2, "price":90, "status":"pending"},
#     {"id":3, "price":120, "status":"paid"},
#     {"id":4, "price":50, "status":"cancelled"}
# ]
# print(order_det(orders))
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         temp = []
#         max_count = 1
#         temp.append(s[0])
#         count = 1
#         if len(s)==0:
#             return 0
#         if len(s)==1:
#             return 1
#         for i in range(1, len(s)):
#             if s[i] not in temp:
#                 count+=1
#                 temp.append(s[i])
#             else:
#                 if count>max_count:
#                     max_count = count
#                 count = 1
#         return max_count
# s = "abcabcbb"
# sol = Solution()
# print(sol.lengthOfLongestSubstring(s))
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         a, b = 1, 2
#         for _ in range(3, n+1):
#             a, b = b, a+b
#         return b
# sol = Solution()
# print(sol.climbStairs(44))

# class Solution:
#     def sortColors(self, nums: list[int]) -> None:
#         for i in range(1, len(nums)):
#             for j in range(0, len(nums)-1):
#                 if nums[j]>nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#
# nums = [2,0,1]
# sol = Solution()
# sol.sortColors(nums)
# print(nums)

# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:
#         rslt = []
#         for i in range(1, n+1):
#             temp = []
#             for j in range(0, k):
#                 temp.append(i)
#             rslt.append(temp)
#         return rslt
#
# sol = Solution()
# # sol.combine(4, 2)
# print(sol.combine(4, 2))

class Solution:
    def largestEven(self, s: str) -> str:
        if not s:
            return ""
        if s[-1] == 2:
            return s
        if len(s) == 1 and s[0] == '1':
            return ""
        while s[-1] != '2':
            s = s[0:len(s) - 1]
            if len(s) == 1:
                break

        return s


sol = Solution()
print(sol.largestEven("1"))
