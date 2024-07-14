def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([6,1,2,3,5,4]))


def selection_sort(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
        arr[i],arr[min_val]=arr[min_val],arr[i]
    return arr
print(selection_sort([6,1,2,3,5,4]))


class Hashtable:
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
        print()
        for i,j in enumerate(self.table):
            print(f"{i}:{j}")
table=Hashtable(10)
arr=[21,12,32,24,45]
for i in  arr:
    table.add(i)
table.display()
print("blaaaa")
print(table.get(24))

class Hashtable:
     def __init__(self,size):
         self.size=size
         self.table=[None]*self.size
     def hash_func(self,key):
         return key%self.size
     def add(self,key):
         index=self.hash_func(key)
         for i in range(self.size):
             new_index=(index+i) % self.size
             if self.table[new_index] is None:
                 self.table[new_index]=key
                 return
         print("full")
     def get(self,key):
         for i in range(self.size):
             index=self.hash_func(key)
             new_index=(index+i)%key
             if self.table[new_index]==key:
                 return new_index
             
             return key%self.size
     def display(self):
         for i,j in enumerate(self.table):
             print(f"{i}:{j}")
table=Hashtable(10)
arr=[21,12,32,24,50,60]
for i in  arr:
    table.add(i)
table.display()
print(table.get(21))


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.top=None
    def push(self,key):
        newnode=node(key)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        self.top=self.top.next
    def pop_specific(self,key):
        temp=self.top
        prev=None
        while(temp is not None and temp.data!=key):
            prev=temp
            temp=temp.next
        prev.next=temp.next
    def middle_delete(self):
        fast=self.top
        slow=self.top
        prev=None
        while(fast is not None and fast.next is not None):
                fast=fast.next.next
                prev=slow
                slow=slow.next
        prev.next=slow.next
    def find_duo(self):
        values=set()
        temp=self.top
        prev=None
        while(temp is not None):
            if temp.data in values:
                prev.next=temp.next
            else:
                values.add(temp.data)
                prev=temp
            temp=temp.next
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
list.push(54)
list.push(14)
list.push(24)
list.push(46)
list.push(51)
list.push(24)
list.display()
print("jjjjjj")
list.find_duo()
list.display()
print("reverse")
list.reverse()
list.display()
print("vagf")
list.pop()
list.display()
print("specific")
list.pop_specific(24)
list.display()
print("middle")
list.middle_delete()
list.display()


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueque(self,key):
        newnode=node(key)
        if self.rear is None:
            self.front=newnode
        else:
            self.rear.next=newnode
        self.rear=newnode
    def dequeque(self):
        if self.front is None:
            print("empty")
        self.front=self.front.next
        if self.rear is None:
            self.rear is None
    def display(self):
        if self.front is None:
            print("empty")
        temp=self.front
        while(temp is not None):
            print(temp.data)
            temp=temp.next
list=SlinkedL()
arr=[1,2,3,4,5,6]
for i in arr:
    list.enqueque(i)
list.display()
print("dequeee")
list.dequeque()
list.display()