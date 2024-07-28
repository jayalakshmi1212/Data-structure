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


# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(0,len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(bubble_sort([6,4,5,3,1,2]))

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# print(insertion_sort([9,10,7,8,5,6]))


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_val=i
#         for j in range(len(arr)):
#             if arr[j]<arr[min_val]:
#                 min_val=j
#             arr[j],arr[min_val]=arr[min_val],arr[j]
#     return arr

# print(selection_sort([9,11,7,8,5,6]))


# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot_elem=arr[0]
#         less_than=[x for x in arr[1:] if x <= pivot_elem]
#         greater_than=[x for x in arr[1:] if x>pivot_elem]
#         return quick_sort(less_than)+[pivot_elem]+quick_sort(greater_than)
# print(quick_sort([1,5,3,4,2]))

# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left_half=arr[:mid]
#         right_half=arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i=j=k=0
#         while( i<len(left_half) and j<len(right_half)):
#             if left_half[i]<right_half[j]:
#                 arr[k]=left_half[i]
#                 i+=1
#             else:
#                 arr[k]=right_half[j]
#                 j+=1
#             k+=1
         
#         while(i<len(left_half)):
#             arr[k]=left_half[i]
#             i+=1
#             k+=1
#         while(j<len(right_half)):
#             arr[k]=right_half[j]
#             j+=1
#             k+=1
#         return arr
# print(merge_sort([13,15,12,14,11]))


# class Hash_table:
#    def __init__(self,size):
#        self.size=size
#        self.table=[None]*self.size
#    def hash_func(self,key):
#        return key%self.size
#    def add(self,key):
#        index=self.hash_func(key)
#        self.table[index]=key
#    def get(self,key):
#        return key%self.size
#    def display(self):
#        for i,j in enumerate(self.table):
#            print(f"{i}:{j}")
# table=Hash_table(10)
# arr=[10,36,28,97,45]
# for i in arr:
#     table.add(i)
# table.display()
# print("getttttt")
# print(table.get(28))
# print("collisionnnnnnnnnnnnnnnnnn")
# class Hash_table:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
#     def hash_func(self,key):
#         return key%self.size
#     def add(self,key):
#         index=self.hash_func(key)
#         for i in range(self.size):
#             new_index=(index+i)%self.size
#             if self.table[new_index] is None:
#                 self.table[new_index]=key
#                 return
#     def get(self,key):
#         index=self.hash_func(key)
#         for i in range(self.size):
#             new_index=(index+1)%self.size
#             if self.table[new_index]==key:
#                 return new_index
#         return index
#     def display(self):
#         for i,j in enumerate(self.table):
#             print(f"{i}:{j}")
# table=Hash_table(10)
# arr=[10,36,28,97,45,20]
# for i in arr:
#     table.add(i)
# table.display()
# print("getttttt")
# print(table.get(20))


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.top=None
#     def push(self,key):
#         newnode=Node(key)
#         if self.top is None:
#             self.top=newnode
#         else:
#             newnode.next=self.top
#             self.top=newnode
#     def pop(self):
#         if self.top is None:
#             return 
#         popped_node=self.top
#         self.top=self.top.next
#         return popped_node.data
#     def display(self):
#         if self.top is None:
#             print("stack underflow")
#         temp=self.top
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
#     def reverse(self):
#         reversed_stack=SlinkedL()
#         while self.top is not None:
#             reversed_stack.push(self.pop())
#         self.top=reversed_stack.top
    
# list=SlinkedL()
# arr=[1,2,3,4,5,6]
# for i in arr:
#     list.push(i)
# list.display()
# print("guluuuuuuuuuuuuu")
# list.reverse()
# list.display()
# print("pop")
# list.pop()
# list.display()


# class Node:
#     def __init__(self,data) : 
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.top=None
#     def push(self,key):
#         newnode=Node(key)
#         if self.top is None:
#             self.top=newnode
#         else:
#             newnode.next=self.top
#             self.top=newnode
#     def pop(self):
#         if self.top is None:
#             return None
#         popped_data=self.top
#         self.top=self.top.next
#         return popped_data.data
#     def middle_remove(self):
#         fast=self.top
#         slow=self.top
#         prev=None
#         while(fast is not None and fast.data is not None):
#             fast=fast.next.next
#             prev=slow
#             slow=slow.next
#         prev.next=slow.next
   
#     def display(self):
#         if self.top is None:
#             print("stack underflow")
#         temp=self.top
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
#     def reverse(self):
#         reversed_stack=SlinkedL()
#         while(self.top is not None ):
#             reversed_stack.push(self.pop())
#         self.top=reversed_stack.top
    
# list=SlinkedL()
# arr=[1,2,3,4,5,6]
# for i in arr:
#     list.push(i)
# list.display()
# # print("pop")
# # list.pop()
# # list.display()
# print("reverse")
# list.reverse()
# list.display()
# print("middle")
# list.middle_remove()
# list.display()



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.rear=None
#         self.front=None
#     def enqueue(self,key):
#         newnode=Node(key)
#         if self.rear is None:
#             self.front=newnode
#         else:
#             self.rear.next=newnode
#         self.rear=newnode
#     def dequeue(self):
#         if self.front is None:
#             return 
#         temp=self.front
#         self.front=self.front.next
#         if self.rear is None:
#             self.rear=None
#     def display(self):
#         if self.front is None:
#             print("empty")
#         temp=self.front
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
# list=SlinkedL()
# arr=[10,20,30,40,50]
# for i in arr:
#     list.enqueue(i)
# list.display()
# print("dequeque")
# list.dequeue()
# list.display()


# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot_elem=arr[0]
#         less_than=[x for x in arr[1:] if x<=pivot_elem]
#         grtr_than=[x for x in arr[1:] if x>pivot_elem]
#         return quick_sort(less_than)+[pivot_elem]+quick_sort(grtr_than)
# print(quick_sort([2,5,3,1,4])),

# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left_half=arr[:mid]
#         right_half=arr[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         i=j=k=0
#         while(i<len(left_half) and j< len(right_half)):
#             if left_half[i]<right_half[j]:
#                 arr[k]=left_half[i]
#                 i+=1
#             else:
#                 arr[k]=right_half[j]
#                 j+=1

#             k+=1
#         while(i<len(left_half)):
#             arr[k]=left_half[i]
#             i+=1
#             k+=1
#         while(j<len(right_half)):
#             arr[k]=right_half[j]
#             j+=1
#             k+=1
#         return arr
# print(merge_sort([2,5,3,1,4]))



# class Hashtable:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
#     def hash_func(self,key):
#         return key%self.size
#     def add(self,key):
#         index=self.hash_func(key)
#         for i in range(self.size):
#             new_index=(index+i)%self.size
#             if self.table[new_index] is None:
#                 self.table[new_index]=key
#                 return
#     def get(self,key):
#         index=self.hash_func(key)
#         for i in range(self.size):
#             new_index=(index+i)%self.size
#             if self.table[new_index]==key:
#                 return new_index
#         return index
#     def remove(self,key):
#         index=self.hash_func(key)
#         for i in range(self.size):
#             new_index=(index+i)%self.size
#             if self.table[new_index]==key:
#                 self.table[new_index]=None
#                 return True
#         return False
#     def display(self):
#         for i,j in enumerate(self.table):
#             print(f"{i}:{j}")
# table=Hashtable(5)
# table.add(10)
# table.add(20)
# table.add(13)
# table.add(65)
# table.display()
# print(table.get(20))
# table.remove(20)
# table.display()


# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
# class Hashtable:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
#     def hash_func(self,key):
#         return key%self.size
#     def add(self,key,value):
#         index=self.hash_func(key)
#         newnode=Node(key,value)
#         if self.table[index] is None:
#             self.table[index]=newnode
#         else:
#             temp=self.table[index]
#             while(temp.next is not None):
#                 temp=temp.next
#             temp.next=newnode
#     def get(self,key):
#         index=self.hash_func(key)
#         current=self.table[index]
#         while(current is not None):
#             if current.key==key:
#                 return current.value
#         return index
#     def remove(self,key):
#         index=self.hash_func(key)
#         current=self.table[index]
#         prev=None
#         while(current is not None):
#             if current.key==key:
#                 if prev is None:
#                     self.table[index]=current.next
#                 else:
#                     prev.next=current.next
#                     return True
#             prev=current
#             current=current.next
#         return False
#     def dup(self):
#         seen=set()
#         dupli=[]
#         for i in self.table:
#             current=i
#             while(current is not None):
#                 if current.key in seen:
#                   dupli.append(current.key)
#                 else:
#                   seen.add(current.key)
#                   current=current.next
#         return dupli


#     def display(self):
#         for i,node in enumerate(self.table):
#             print(f"{i}::",end=" ")
#             current=node
#             while(current is not None):
#                 print(f"{current.key}:{current.value}",end="-->")
#                 current=current.next
#             print("none")
# table=Hashtable(5)
# table.add(10,"hello")
# table.add(10,"hell")
# table.add(20,"haai")
# table.add(22,"h00i")
# table.add(25,"hiiii")
# table.display()
# print(table.get(22))
# table.remove(22)
# table.display()
# print(table.dup())

            

       
        
# #######################bubble sort##############################
# def bubble_sort(arr):
#    for i in range(len(arr)-1):
#       for j in range(len(arr)-1-i):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
        
#    return arr
# print(bubble_sort([3,4,2,5,1]))

# def bubble_sort(arr):
#    i=0
#    while(i<len(arr)-1):
#       j=0
#       while(j<len(arr)-1-i):
#          if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#          j+=1
#       i+=1
#    return arr
# print(bubble_sort([3,4,2,5,1]))
# #################################### insertion ####################################
# def insertion_sort(arr):
#    for i in range(len(arr)):
#       key=arr[i]
#       j=i-1
#       while(j>=0 and key<arr[j]):
#          arr[j+1]=arr[j]
#          j-=1
#       arr[j+1]=key
#    return arr
# print(insertion_sort([6,9,7,10,8]))

# def insertion_sort(arr):
#    i=0
#    while(i<len(arr)):
#       key=arr[i]
#       j=i-1
#       while(j>=0 and key<arr[j]):
#           arr[j+1]=arr[j]
#           j-=1
#       i+=1
#       arr[j+1]=key
      
#    return arr
# print(insertion_sort([6,9,7,10,8]))
# #################################### selection ##########################################3
# def selection_sort(arr):
#    for i in range(len(arr)):
#       min_val=i
#       for j in range(i+1,len(arr)):
#          if arr[j]<arr[min_val]:
#             min_val=j
#       arr[i],arr[min_val]=arr[min_val],arr[i]
#    return arr
# print(selection_sort([12,14,11,15,13]))

# def selection_sort(arr):
#    i=0
#    while(i<len(arr)):
#       min_val=i
#       j=i+1
#       while(j<len(arr)):
#          if arr[j]<arr[min_val]:
#             min_val=j
#          j+=1
#       arr[i],arr[min_val]=arr[min_val],arr[i]
#       i+=1
#    return arr
# print(selection_sort([12,14,11,15,13]))
# ################################ quick ##################################
# def quick_sort(arr):
#    if len(arr)<1:
#       return arr
#    else:
#       pivot_elem=arr[0]
#       less_than=[x for x in arr[1:] if x<pivot_elem]
#       greater_than=[x for x in arr[1:] if x>pivot_elem]
#       return quick_sort(less_than)+[pivot_elem]+quick_sort(greater_than)
# print(quick_sort([19,16,20,18,17]))
# ################################ merge ###################################3
# def merge_sort(arr):
#    if len(arr)>1:
#       mid=len(arr)//2
      
#       left_half=arr[:mid]
#       right_half=arr[mid:]

#       merge_sort(left_half)
#       merge_sort(right_half)

#       i=j=k=0

#       while(i<len(left_half) and j<len(right_half)):
#          if left_half[i]<right_half[j]:
#             arr[k]=left_half[i]
#             i+=1
#          else:
#             arr[k]=right_half[j]
#             j+=1
#          k+=1

#       while(i<len(left_half)):
#          arr[k]=left_half[i]
#          i+=1
#          k+=1
#       while(j<len(right_half)):
#          arr[k]=right_half[j]
#          j+=1
#          k+=1
#       return arr
# print(merge_sort([22,24,21,23,25]))


# #################################  stack ################################
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
#          return None
#       popped_node=self.top
#       self.top=self.top.next
#       return popped_node.data
#    def middle_elem(self):
#       slow=self.top
#       fast=self.top
#       prev=None
#       while(fast is not None and fast.next is not None):
#          fast=fast.next.next
#          prev=slow
#          slow=slow.next
#       return slow.data
#    def dup(self):
#       seen=set()
#       duplicate=[]
#       tem=self.top
#       while(tem is not None):
#          if tem.data in seen:
#             duplicate.append(tem.data)
#          else:
#             seen.add(tem.data)
#          tem=tem.next
#       return  duplicate
#    def even(self):
#       tem=self.top
#       even=[]
#       while(tem is not None):
#          if tem.data%2==0:
#             even.append(tem.data)
#          tem=tem.next
#       return even
#    def display(self):
#       if self.top is None:
#          print("empty")
#       temp=self.top
#       while(temp is not None):
#          print(temp.data)
#          temp=temp.next
#    def reverse(self):
#       reversed_stack=SlinkedL()
#       while self.top is not None:
#             reversed_stack.push(self.pop())
#       self.top=reversed_stack.top
# list=SlinkedL()
# arr=[1,2,4,7,3,4,5]
# for i in arr:
#    list.push(i)
# list.display()
# print("middle")
# print(list.middle_elem())
# list.pop()
# list.display()
# print("reverse")
# list.reverse()
# list.display()
# print(list.dup())
# print(list.even())


# class queue:
#    def __init__(self):
#       self.stack=[]
#       self.stack2=[]
#    def enqueue(self,element):
#       self.stack.append(element)
#    def dequeue(self):
#       if not self.stack2:
#          while self.stack:
#             self.stack2.append(self.stack.pop())
#       return self.stack2.pop()
#    def peek(self):
#       if not self.stack2:
#          while(self.stack):
#             self.stack2.append(self.stack.pop())
#       return self.stack2[-1]
# que=queue()
# que.enqueue(1)
# que.enqueue(2)
# que.enqueue(3)
# print(que.stack)
# print(que.dequeue())
# print(que.peek())

# class stack:
#    def __init__(self) :
#       self.queue=[]
#       self.queue2=[]
#    def push(self,element):
#       self.queue.append(element)
#    def pop(self):
#       while len(self.queue)>1:
#          self.queue2.append(self.queue.pop(0))
#       popped_elem=self.queue.pop(0)
#       return popped_elem

# mystack=stack()
# mystack.push(1)
# mystack.push(2)
# mystack.push(3)
# print(mystack.pop())
# print(mystack.queue2)



# class Node:
#    def __init__(self,data) :
#       self.data=data
#       self.next=None
# class SlinkedL:
#    def __init__(self):
#       self.rear=None
#       self.front=None
#    def enqueue(self,key):
#       newnode=Node(key)
#       if self.rear is None:
#          self.front=newnode
#       else:
#          self.rear.next=newnode
#       self.rear=newnode
#    def dequeue(self):
#       self.front=self.front.next
#    def display(self):
#       if self.front is None:
#           print("empty")
#       temp=self.front
#       while(temp is not None):
#          print(temp.data)
#          temp=temp.next
# list=SlinkedL()
# list.enqueue(1)
# list.enqueue(2)
# list.enqueue(3)
# list.display()
# list.dequeue()
# list.display()

# class Node:
#    def __init__(self,key):
#       self.key=key
#       self.next=None
# class Hashtable:
#    def __init__(self,size):
#       self.size=size
#       self.table=[None]*self.size
#    def hash_func(self,key):
#       return key%self.size
#    def add(self,key):
#       index=self.hash_func(key)
#       newnode=Node(key)
#       if self.table[index] is None:
#          self.table[index]=newnode
#       else:
#          temp=self.table[index]
#          while(temp.next is not None):
#             temp=temp.next
#          temp.next=newnode
#    def get(self,key):
#       index=self.hash_func(key)
#       current=self.table[index]
#       while(current is not None and current.key!=key):
#              print("not exist")
#              current=current.next
#              return
#       return index
      
#    def remove(self,key):
#       index=self.hash_func(key)
#       current=self.table[index]
#       prev=None
#       while(current is not None ):
#          if current.key==key:
#             if prev is None:
#                self.table[index]=current.next
#             else:
#                prev.next=current.next
#             return True
#          prev=current
#          current=current.next
#       return False
         
#    def display(self):
#       for i,node in enumerate(self.table):
#          print(f"{i}:",end="")
#          current=node
#          while(current is not None):
#             print(f"{current.key}",end="-->")
#             current=current.next
#          print("None")
# table=Hashtable(5)
# arr=[10,20,56,17]
# for i in arr:
#    table.add(i)
# table.display()
# print(table.get(17))
# table.remove(17)
# table.display()


# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(bubble_sort([2,1,4,3,5]))

# def bubble_sort(arr):
#     i=0
#     while(i<len(arr)-1):
#         j=0
#         while(j<len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#             j+=1
#         i+=1
#     return arr
# print(bubble_sort([2,1,4,3,5]))

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# print(insertion_sort([8,6,10,9,7]))

# def insertion_sort(arr):
#     i=1
#     while(i<len(arr)):
#         key=arr[i]
#         j=i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1]=arr[j]
#             j-=1
#         i+=1
#         arr[j+1]=key
#     return arr
# print(insertion_sort([8,6,10,9,7]))

# def selction_sort(arr):
#     for i in range(len(arr)):
#         min_val=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min_val]:
#                 min_val=j
#             arr[i],arr[min_val]=arr[min_val],arr[i]
#     return arr
# print(selction_sort([11,14,15,13,12]))


# def selection_sort(arr):
#     i=0
#     while(i<len(arr)):
#         min_val=i
#         j=i+1
#         while(j<len(arr)):
#             if arr[j]<arr[min_val]:
#                 min_val=j
#             j+=1
#             arr[i],arr[min_val]=arr[min_val],arr[i]
#         i+=1
#     return arr   
# print(selction_sort([11,14,15,13,12]))

# def quick_sort(arr):
#     if len(arr)<1:
#         return arr
#     else:
#         pivot_elem=arr[0]
#         less_than=[x for x in arr[1:] if x<pivot_elem]
#         greater_than=[x for x in arr[1:] if x>pivot_elem]
#         return quick_sort(less_than)+[pivot_elem]+quick_sort(greater_than)
# print(quick_sort([18,20,16,19,17]))


# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
        
#         left_half=arr[:mid]
#         right_half=arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i=j=k=0
#         while(i<len(left_half) and j<len(right_half)):
#             if left_half[i]<right_half[j]:
#                 arr[k]=left_half[i]
#                 i+=1
#             else:
#                 arr[k]=right_half[j]
#                 j+=1
#             k+=1
#         while(i<len(left_half)):
#             arr[k]=left_half[i]
#             i+=1
#             k+=1
#         while(j<len(right_half)):
#             arr[k]=right_half[j]
#             j+=1
#             k+=1
#         return arr
# print(merge_sort([18,20,16,19,17]))


# class queue:
#     def __init__(self):
#         self.stack=[]
#         self.stack2=[]
#     def enqueue(self,element):
#         self.stack.append(element)
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack:
#                 self.stack2.append(self.stack.pop())
#         return self.stack2.pop()
#     def peek(self):
#         if not self.stack2:
#             while self.stack:
#                 self.stack2.append(self.stack.pop())
#         return self.stack2[-1]
# q=queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.stack2)
# print(q.peek())


# class stack:
#     def __init__(self):
#         self.queue=[]
#         self.queue2=[]
#     def push(self,element):
#         self.queue.append(element)
#     def pop(self):
#         while(len(self.queue)>1):
#             self.queue2.append(self.queue.pop(0))
#         popped_elem=self.queue.pop(0)
#         return popped_elem
# mystack=stack()
# mystack.push(1)
# mystack.push(2)
# mystack.push(3)
# print(mystack.pop())
# print(mystack.queue2)


# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.next=None
# class Hashtable:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
#     def hash_func(self,key):
#         return key%self.size
#     def add(self,key):
#         index=self.hash_func(key)
#         newnode=Node(key)
#         if self.table[index] is None:
#             self.table[index]=newnode
#         else:
#             temp=self.table[index]
#             while(temp.next is not None ):
#                 temp=temp.next
#             temp.next=newnode
#     def get(self,key):
#         index=self.hash_func(key)
#         temp=self.table[index]
#         while(temp is not None and temp.key!=key):
#             temp=temp.next
#             if temp.key==key:
#                 return index
#         return index
#     def remove(self,key):
#         index=self.hash_func(key)
#         temp=self.table[index]
#         prev=None
#         while(temp is not None ):
#             if temp.key==key:
#                 if prev is None:
#                     self.table[index]=temp.next
#                 else:
#                     prev.next=temp.next
#                     return True
#             prev=temp
#             temp=temp.next
#         return False
#     def display(self):
#         for i,node in enumerate(self.table):
#             print(f"{i}:",end="")
#             current=node
#             while(current is not None):
#                 print(f"{current.key}",end="-->")
#                 current=current.next
#             print("none")
# table=Hashtable(5)
# table.add(10)
# table.add(20)
# table.add(12)
# table.add(21)
# table.display()
# print(table.get(20))
# table.remove(20)
# table.display()
                  


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.top=None
#     def push(self,key):
#         newnode=Node(key)
#         if self.top is None:
#             self.top=newnode
#         else:
#             newnode.next=self.top
#             self.top=newnode
#     def pop(self):
#         if self.top is None:
#             return None
#         popped_data=self.top
#         self.top=self.top.next
#         return popped_data.data
#     def display(self):
#         if self.top is None:
#             print("empty")
#         temp=self.top
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
#     def reverse(self):
#         reversed_stack=SlinkedL()
#         while self.top is not None:
#             reversed_stack.push(self.pop())
#         self.top=reversed_stack.top
# list=SlinkedL()
# arr=[1,2,3,4,5]
# for i in arr:
#     list.push(i)
# list.display()
# list.pop()
# list.display()
# print("reverse")
# list.reverse()
# list.display()
            

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.rear=None
#         self.front=None
#     def enqueue(self,key):
#         newnode=Node(key)
#         if self.rear is None:
#             self.top=newnode
#         else:
#             self.rear.next=newnode
#         self.rear=newnode
#     def dequeue(self):
#         if self.rear is None:
#             print("empty")
         



class TrieNode:
    def __init__(self):
        self.children={}
        self.wordend=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word:str):
        current=self.root
        for c in word:
            if c  not in current.children:
                current.children[c]=TrieNode()
            current=current.children[c]
        current.wordend=True

    def search(self,word:str):
        current=self.root
        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        return current.wordend
    
    def startwith(self,prefix:str):
        current=self.root
        for c in prefix:
            if c not in current.children:
                return False
            current=current.children[c]
        return True
    


class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data>key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    
    def search(self,key):
        if self.data==key:
            print("data found")
        if self.data>key:
            if self.lchild:
                self.lchild.search(key)
            else:
               print("data is not found")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("data is not found")  

    def delete(self,key):
        if self.data is None:
            print("empty")
        if self.data>key:
            if self.lchild:
                self.lchild=self.lchild.delete(key)
            else:
                print("data not found")
        elif self.data<key:
            if self.rchild:
                self.rchild=self.rchild.delete(key)
            else:
                print("data not found")
        else:
            if self.lchild is None and self.rchild is None:
                return 
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(node.data)
    
    def min_val(self):
        current=self
        while current.lchild:
            current=current.lchild
        return current.data
    
    def max_val(self):
        current=self
        while current.rchild:
            current=current.rchild
        return current.data

    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

root=BST(10)
arr=[1,2,12,3]
root.preorder()
for i in arr:
    root.insert(i)
root.delete(2)
if root:
   root.preorder()
else:
    print("it is not containing the value")
print("max val:")
print(root.max_val())
print("min_val:")
print(root.min_val())



class max_heap:
    def __init__(self):
        self.heap=[]
    def parent(self,index):
        return (index-1)//2
    def left_child(self,index):
        return 2*index+1
    def right_child(self,index):
        return 2*index+2
    def heapify_up(self,index):
        parent=self.parent(index)
        if index>0 and self.heap[index]>self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self,index):
        left=self.left_child(index)
        right=self.right_child(index)
        largest=index

        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if index!=largest:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self.heapify_down(largest)
    def extract_max(self):
        if self.heap  is None:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    def max_peek(self):
        return self.heap[0] if self.heap else None
    
    def __str__(self):
        return str(self.heap)
    

maxhp=max_heap()
maxhp.insert(10)
maxhp.insert(5)
maxhp.insert(2)
maxhp.insert(3)
maxhp.insert(20)
print(maxhp)
print(maxhp.extract_max())
print(maxhp)
print(maxhp.max_peek())


