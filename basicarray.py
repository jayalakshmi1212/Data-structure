# sum of array 
# arr = [1, -1, 3, -3, 5]
# class solution:
#     def sum(self,n,arr):
#         for i in arr:
#             n+=i
#         return n
    
# sol=solution()
# result=sol.sum(0,arr)
# print(result)

#Print an array in reverse order
# class solution:
#     def reverse(self,n,arr):
#         n=arr[::-1]
#         return n
# sol=solution()
# result=sol.reverse(0,arr)
# print(result)
    
#Replace all negative elements in the array with zeros.
# class Solution:
#     def neg_elem(self, arr):
#         for i in range(len(arr)):
#             if arr[i] == -i:
#                 arr[i] = 0
# sol = Solution()
# sol.neg_elem(arr)
# print(arr)

#largest number
# for i in range(len(arr)):
#     largest_num=arr[0]
#     if arr[i]>=largest_num:
#         largest_num=arr[i]
# arr.sort(reverse=True)
# print(largest_num)

#smallest number

# for i in range(len(arr)):
#     smallest_num=arr[0]
#     if arr[i]<=smallest_num:
#         smallest_num=arr[i]
# arr.sort()
# print(smallest_num)

# def sumoftarget(arr,target):
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
                #  return arr[i],arr[j]      #complexity=o(n^2)
#     return None

# arr=[5,6,7,8,4,9]
# target=10
# result=sumoftarget(arr,target)                                    
# print(result)

# def sumoftarget(arr,target):
#     seto=set()  
#     for i in  arr:
#         num=target-i
#         if num in seto:
#             return num,i             #complexit=o(n)
#         seto.add(i)       
#     return None 
# arr=[5,6,7,8,4,9]
# target=10
# result=sumoftarget(arr,target)                                    
# print(result)
