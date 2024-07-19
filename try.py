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
# def bubble_sort(arr):
#    for i in range(len(arr)-1):
#       for j in range(0,len(arr)-1-i):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#    return arr
# print(bubble_sort([5,4,3,2,1]))

# def opti_bubb_sort(arr):
#    for i in range(len(arr)-1):
#       swapped=False
#       for j in range(len(arr)-1-i):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             swapped=True
#       if not swapped:
#          break
#    return arr
# print(opti_bubb_sort([5,4,3,2,1]))


# class Node:
#    def __init__(self,data):
#       self.data=data
#       self.next=None
# class SlinkedL:
#    def __init__(self):
#       self.top=None
#    def push(self,key):
#       newnode=Node(key)
#       if self.top is None:
#          self.top=newnode
#       else:
#          newnode.next=self.top
#          self.top=newnode
#    def pop(self):
#       if self.top is None:
#          print("stack underflow")
#       self.top=self.top.next
#    def remove_middle(self):
#       fast=self.top
#       slow=self.top
#       prev=None
#       while(fast is not None and fast.next is not None):
#          fast=fast.next.next
#          prev=slow
#          slow=slow.next
#       prev.next=slow.next
#    def display(self):
#       if self.top is None:
#          print("empty")
#       temp=self.top
#       while(temp is not None):
#          print(temp.data)
#          temp=temp.next
#    def reverse(self):
#       temp=self.top
#       prev=None
#       while(temp is not None):
#          next=temp.next
#          temp.next=prev
#          prev=temp
#          temp=next
#       self.top=prev
# list=SlinkedL()
# arr=[1,2,3,4,5,6]
# for i in arr:
#    list.push(i)
# list.display()
# print("tanjiro")
# list.pop()
# list.display()
# print("nezuko")
# list.remove_middle()
# list.display()


# class node:
#    def __init__(self,data):
#       self.data=data
#       self.next=None
# class SlinkedL:
#    def __init__(self):
#       self.front=None
#       self.rear=None
#    def enqueue(self,key):
#       newnode=node(key)
#       if self.rear is None:
#          self.front=newnode
#       else:
#          self.rear.next=newnode
#       self.rear=newnode
#    def dequeue(self):
#        if self.front is None:
#             print("empty")
#        self.front=self.front.next
#        if self.rear is None:
#             self.rear=None
#    def display(self):
#       if self.front is None:
#          print("empty")
#       temp=self.front
#       while(temp is not None):
#          print(temp.data)
#          temp=temp.next
# list=SlinkedL()
# arr=[1,2,3,4,5]
# for i in arr:
#    list.enqueue(i)
# list.display()


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([6,4,5,3,1,2]))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([9,10,7,8,5,6]))


def selection_sort(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
            arr[j],arr[min_val]=arr[min_val],arr[j]
    return arr

print(selection_sort([9,11,7,8,5,6]))


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot_elem=arr[0]
        less_than=[x for x in arr[1:] if x <= pivot_elem]
        greater_than=[x for x in arr[1:] if x>pivot_elem]
        return quick_sort(less_than)+[pivot_elem]+quick_sort(greater_than)
print(quick_sort([1,5,3,4,2]))

def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0
        while( i<len(left_half) and j<len(right_half)):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1
         
        while(i<len(left_half)):
            arr[k]=left_half[i]
            i+=1
            k+=1
        while(j<len(right_half)):
            arr[k]=right_half[j]
            j+=1
            k+=1
        return arr
print(merge_sort([13,15,12,14,11]))


class Hash_table:
   def __init__(self,size):
       self.size=size
       self.table=[None]*self.size
   def hash_func(self,key):
       return key%self.size
   def add(self,key):
       index=self.hash_func(key)
       self.table[index]=key
   def get(self,key):
       return key%self.size
   def display(self):
       for i,j in enumerate(self.table):
           print(f"{i}:{j}")
table=Hash_table(10)
arr=[10,36,28,97,45]
for i in arr:
    table.add(i)
table.display()
print("getttttt")
print(table.get(28))
print("collisionnnnnnnnnnnnnnnnnn")
class Hash_table:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash_func(self,key):
        return key%self.size
    def add(self,key):
        index=self.hash_func(key)
        for i in range(self.size):
            new_index=(index+i)%self.size
            if self.table[new_index] is None:
                self.table[new_index]=key
                return
    def get(self,key):
        index=self.hash_func(key)
        for i in range(self.size):
            new_index=(index+1)%self.size
            if self.table[new_index]==key:
                return new_index
        return index
    def display(self):
        for i,j in enumerate(self.table):
            print(f"{i}:{j}")
table=Hash_table(10)
arr=[10,36,28,97,45,20]
for i in arr:
    table.add(i)
table.display()
print("getttttt")
print(table.get(20))


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
            return 
        popped_node=self.top
        self.top=self.top.next
        return popped_node.data
    def display(self):
        if self.top is None:
            print("stack underflow")
        temp=self.top
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        reversed_stack=SlinkedL()
        while self.top is not None:
            reversed_stack.push(self.pop())
        self.top=reversed_stack.top
    
list=SlinkedL()
arr=[1,2,3,4,5,6]
for i in arr:
    list.push(i)
list.display()
print("guluuuuuuuuuuuuu")
list.reverse()
list.display()
print("pop")
list.pop()
list.display()


class Node:
    def __init__(self,data) : 
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
            return None
        popped_data=self.top
        self.top=self.top.next
        return popped_data.data
    def middle_remove(self):
        fast=self.top
        slow=self.top
        prev=None
        while(fast is not None and fast.data is not None):
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
   
    def display(self):
        if self.top is None:
            print("stack underflow")
        temp=self.top
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        reversed_stack=SlinkedL()
        while(self.top is not None ):
            reversed_stack.push(self.pop())
        self.top=reversed_stack.top
    
list=SlinkedL()
arr=[1,2,3,4,5,6]
for i in arr:
    list.push(i)
list.display()
# print("pop")
# list.pop()
# list.display()
print("reverse")
list.reverse()
list.display()
print("middle")
list.middle_remove()
list.display()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueue(self,key):
        newnode=Node(key)
        if self.rear is None:
            self.front=newnode
        else:
            self.rear.next=newnode
        self.rear=newnode
    def dequeue(self):
        if self.front is None:
            return 
        temp=self.front
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
arr=[10,20,30,40,50]
for i in arr:
    list.enqueue(i)
list.display()
print("dequeque")
list.dequeue()
list.display()


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot_elem=arr[0]
        less_than=[x for x in arr[1:] if x<=pivot_elem]
        grtr_than=[x for x in arr[1:] if x>pivot_elem]
        return quick_sort(less_than)+[pivot_elem]+quick_sort(grtr_than)
print(quick_sort([2,5,3,1,4])),

def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while(i<len(left_half) and j< len(right_half)):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1

            k+=1
        while(i<len(left_half)):
            arr[k]=left_half[i]
            i+=1
            k+=1
        while(j<len(right_half)):
            arr[k]=right_half[j]
            j+=1
            k+=1
        return arr
print(merge_sort([2,5,3,1,4]))


