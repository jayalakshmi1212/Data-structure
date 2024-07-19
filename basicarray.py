# # sum of array 
# arr = [1, -1, 3, -3, 5]
# class solution:
#     def sum(self,n,arr):
#         for i in arr:
#             n+=i
#         return n
    
# sol=solution()
# result=sol.sum(0,arr)
# print(result)

# # Print an array in reverse order
# class solution:
#     def reverse(self,n,arr):
#         n=arr[::-1]
#         return n
# sol=solution()
# result=sol.reverse(0,arr)
# print(result)
    
# # Replace all negative elements in the array with zeros.
# class Solution:
#     def neg_elem(self, arr):
#         for i in range(len(arr)):
#             if arr[i] == -i:
#                 arr[i] = 0
# sol = Solution()
# sol.neg_elem(arr)
# print(arr)

# # largest number
# for i in range(len(arr)):
#     largest_num=arr[0]
#     if arr[i]>=largest_num:
#         largest_num=arr[i]
# arr.sort(reverse=True)
# print(largest_num)

# # smallest number

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
#                  return arr[i],arr[j]      #complexity=o(n^2)
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

# def reverse_array(arr):
#     start=0
#     end=len(arr)-1
#     while(start<end):
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1
#     return arr
# arr=[1,2,3,4,5]
# reversed_arr=reverse_array(arr)
# print(reversed_arr)

# def largest(arr):
#     largest=arr[0]
#     for i in range(len(arr)):
#         if arr[i]>largest:
#             largest=arr[i]
#     return largest
# print(largest([1,2,3,4,6,5,7]))

# def smallest(arr):
#     smallest=arr[0]
#     for i in range(len(arr)):
#         if arr[i]<arr[0]:
#             smallest=arr[i]
#     return smallest
# print(smallest([5,6,2,1,0,9]))


# def neg_elem_by_0(arr):
#     for i in range(len(arr)):
#         if arr[i]<0:
#            arr[i]=0
#     return arr
# print(neg_elem_by_0([1,2,-3,4,-5]))


# def avg_of_elem(arr):
#     n=0
#     v=0
#     for i in arr:
#         n+=i
#         v+=1
#     return n//v
# print(avg_of_elem([1,2,3,4,5]))


# def avg_of_even_elem(arr):
#     n=0
#     v=0
#     for i in arr:
#         if i%2==0:
#             n+=i
#             v=+1
#     return n//v
# print(avg_of_elem([1,2,3,4,5]))


# def avg_of_odd_elem(arr):
#     n=0
#     v=0
#     for i in arr:
#         if i%2!=0:
#             n+=i
#             v=+1
#     return n//v
# print(avg_of_elem([1,2,3,4,5]))


            
# def second_largest(arr):
#      largest=arr[0]
#      second_largest=0
#      for i in range(len((arr))):
#          if arr[i]>largest:
#              second_largest=largest
#              largest=arr[i]
#          elif arr[i]>second_largest and arr[i]!=largest:
#              second_largest=arr[i]
#      return second_largest
# print(second_largest([1,4,5,6,2]))

# def second_smallest(arr):
#     smallest=arr[0]
#     second_smallest=
#     for i in range(len(arr)):
#         if arr[i]<smallest:
#             second_smallest=smallest
#             smallest=arr[i]
#         elif arr[i]<second_smallest and arr[i]!=smallest:
#             second_smallest=arr[i]
#     return second_smallest
# print(second_smallest([1,4,5,6,2]))

def find_uncommon(arr1,arr2):
    uncommon_elem=[]
    for i in arr1:
        if i not in arr2:
            uncommon_elem.append(i)
    for i in arr2:
        if i not in arr1:
            uncommon_elem.append(i)
    return uncommon_elem
arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]
print(find_uncommon(arr1,arr2))
       

def sorted_or_not(arr):
    for i in range(len(arr)-1):
       if arr[i]>arr[i+1]:
        return False
    return True
print(sorted_or_not([1,2,5,9]))