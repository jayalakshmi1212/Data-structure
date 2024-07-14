# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self) :
#          self.head=None
#          self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def insertbeg(self,key):
#         newnode=Node(key)
#         newnode.next=self.head
#         self.head=newnode
#     def insaft(self,nexto,key):
#         newnode=Node(key)
#         temp=self.head
#         prev=None
#         while(temp is not None and temp.data!=nexto):
#             temp=temp.next
#         if self.tail==nexto:
#             self.tail.next=newnode
#             self.tail=newnode
#             self.tail.next=None
#         newnode.next=temp.next
#         temp.next=newnode
#     def delete(self,key):
#         temp=self.head
#         prev=None
#         if(temp.data==key):
#             self.head=temp.next
#             return
#         while(temp is not None and temp.data!=key):
#             prev=temp
#             temp=temp.next
#         if temp is None:
#             return
#         if(temp==self.tail):
#             self.tail=prev
#             self.tail.next=None
#             return
#         prev.next=temp.next
#     def middle(self):
#         if self.head is None:
#             self.head=None
#             return
#         fast=self.head
#         slow=self.head
#         prev=None
#         while(fast is not None and fast.next is not None):
#             fast=fast.next.next
#             prev=slow
#             slow=slow.next
#         prev.next=slow.next

#     def display(self):
#         if self.head is None:
#             print("list is empty")
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
#     def reverse(self):
#         temp=self.head
#         prev=None
#         while(temp is not None):
#             next=temp.next
#             temp.next=prev
#             prev=temp
#             temp=next
#         self.head=prev
# list=SlinkedL()
# arr=[1,2,3,4,5,6]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("inb")
# list.insertbeg(3)
# list.display()
# print('blaaaaaaaaaaaaa')
# list.insaft(4,7)
# list.display()
# print("laaaaaaaaaaaaaaaaa")
# list.delete(7)
# list.display()
# print("klaaaaaaaaaaa")
# list.reverse()
# list.display()
# print("klee")
# list.middle()
# list.display()

# print("biiii")
# def binary_search(arr,target):
#     left,right=0,len(arr)
#     mid=left+right//2
#     while(left<=right):
#         if arr[mid]==target:
#             return mid
#         if arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# print(binary_search([1,2,3,4,5],3))


# def palindrome(arr):
#     if len(arr)<=1:
#         return True
#     if arr[0]!=arr[-1]:
#         return False
#     return palindrome(arr[1:-1])
# print(palindrome("racecar"))

# def factorial(arr):
#     if arr<=1:
#        return 1
#     return arr*factorial(arr-1)
# print(factorial(5))

# def sum(arr):
#     if not arr:
#         return 0
#     return arr[0]+sum(arr[1:])
# print(sum([1,2,3,4,5]))

# def binary_search_recur(arr,target,left,right):
#     if left>right:
#         return -1
#     mid=(left+right)//2
#     if arr[mid]==target:
#         return mid
#     elif arr[mid]<target:
#         return binary_search_recur(arr,target,mid+1,right)
#     else:
#         return binary_search_recur(arr,target,left,mid-1)
# def binary_search(arr,target):
#     return binary_search_recur(arr,target,0,len(arr)-1)
# arr=[1,2,3,4,5]
# target=3
# print(binary_search(arr,target))
def bubble_sort(arr):
   for i in range(len(arr)-1):
      for j in range(0,len(arr)-1-i):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
   return arr
print(bubble_sort([5,4,3,2,1]))

def opti_bubb_sort(arr):
   for i in range(len(arr)-1):
      swapped=False
      for j in range(len(arr)-1-i):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
      if not swapped:
         break
   return arr
print(opti_bubb_sort([5,4,3,2,1]))


class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
class SlinkedL:
   def __init__(self):
      self.top=None
   def push(self,key):
      newnode=Node(key)
      if self.top is None:
         self.top=newnode
      else:
         newnode.next=self.top
         self.top=newnode
   def pop(self):
      if self.top is None:
         print("stack underflow")
      self.top=self.top.next
   def remove_middle(self):
      fast=self.top
      slow=self.top
      prev=None
      while(fast is not None and fast.next is not None):
         fast=fast.next.next
         prev=slow
         slow=slow.next
      prev.next=slow.next
   def display(self):
      if self.top is None:
         print("empty")
      temp=self.top
      while(temp is not None):
         print(temp.data)
         temp=temp.next
   def reverse(self):
      temp=self.top
      prev=None
      while(temp is not None):
         next=temp.next
         temp.next=prev
         prev=temp
         temp=next
      self.top=prev
list=SlinkedL()
arr=[1,2,3,4,5,6]
for i in arr:
   list.push(i)
list.display()
print("tanjiro")
list.pop()
list.display()
print("nezuko")
list.remove_middle()
list.display()


class node:
   def __init__(self,data):
      self.data=data
      self.next=None
class SlinkedL:
   def __init__(self):
      self.front=None
      self.rear=None
   def enqueue(self,key):
      newnode=node(key)
      if self.rear is None:
         self.front=newnode
      else:
         self.rear.next=newnode
      self.rear=newnode
   def dequeue(self):
       if self.front is None:
            print("empty")
       self.front=self.front.next
       if self.rear is None:
            self.rear=None
   def display(self):
      if self.front is None:
         print("empty")
      temp=self.front
      while(temp is not None):
         print(temp.data)
         temp=temp.next
list=SlinkedL()
arr=[1,2,3,4,5]
for i in arr:
   list.enqueue(i)
list.display()