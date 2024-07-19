class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
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
            new_index=(index+i)%self.size
            if self.table[new_index]==key:
                return new_index
        return index
    def finddup(self):
         seen=set()
         duplicates=[]
         for i in self.table:
             if i in seen:
                 duplicates.append(i)
             else:
                 seen.add(i)
         return duplicates
    def display(self):
        for i,j in enumerate(self.table):
            print(f"{i}::{j}")
table=Hashtable(8)
arr=[16,24,45,11,52,11]
for i in arr:
    table.add(i)
table.display()
print(table.get(45))
print(table.finddup())

class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash_func(self,key):
        return key%self.size
    def add(self,key):
        index=self.hash_func(key)
        new_node=Node(key)
        if self.table[index] is None:
            self.table[index]=new_node
        else:
            temp=self.table[index]
            while(temp.next is not None):
                temp=temp.next
            temp.next=new_node
    def get(self,key):
        index=self.hash_func(key)
        temp=self.table[index]
        while(temp is not None and temp.key!=key):
            temp=temp.next
        return index
    def display(self):
        for i,node in enumerate(self.table):
            print(f"index {i}:",end=" ")
            current=node
            while(current is not None):
                print(f"{current.key}",end="-->")
                current=current.next
            print("None")
table=Hashtable(10)
arr=[10,20,30,34,54,67,81]
for i in arr:
    table.add(i)
table.display()
print(table.get(67))


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0

        while(i<len(left_half) and j<len(right_half)):
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
print(merge_sort([2,5,6,1,8,3])) 


def quick_sort(arr):
    if len(arr)<1:
        return arr
    else:
        pivot_elem=arr[0]
        less_than=[x for x in arr[1:] if x<pivot_elem]
        greater=[x for x in arr[1:] if x>pivot_elem]
        return quick_sort(less_than)+[pivot_elem]+quick_sort(greater)
print(quick_sort([5,3,1,4,2]))


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
        popped_node=self.top
        self.top=self.top.next
        return popped_node.data

    def display(self):
        if self.top is None:
            print("empty")
        temp=self.top
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        reverse_stack=SlinkedL()
        while self.top is not None:
            reverse_stack.push(self.pop())
        self.top=reverse_stack.top
list=SlinkedL()
arr=[1,2,3,4,5]
for i in arr:
    list.push(i)
list.display()
print("hyhjhjkoiui")
list.reverse()
list.display()
list.pop()
list.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueque(self,key):
        newnode=Node(key)
        if self.rear is None:
            self.front=newnode
        else:
            self.rear.next=newnode
        self.rear=newnode
    def dequeque(self):
          self.front=self.front.next
    def display(self):
        if self.front is None:
            print("empty")
        temp=self.front
        while(temp is not None):
            print(temp.data) 
            temp=temp.next
print("queueueueueue")  
list=SlinkedL()
arr=[1,2,3,4,5]
for i in arr:
    list.enqueque(i)
list.display()
list.dequeque()
list.display()

# ########################### bubble sort ########################
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([5,3,2,4,1]))

def bubble_sort(arr):
    i=0
    while(i<len(arr)-1):
        j=0
        while(j<len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            j+=1
        i+=1
    return arr
print(bubble_sort([5,3,2,4,1]))

#################  Insertion sort  ###########################
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([5,3,2,4,1]))


def insertion_sort(arr):
    i=1
    while(i<len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        i+=1
    return arr
print(insertion_sort([5,3,2,4,1]))


########################### selection sort #####################
def selection_sort(arr):
    for i in range(len(arr)):
        min_val=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_val]:
                min_val=j
        arr[i],arr[min_val]=arr[min_val],arr[i]
      
    return arr
print(selection_sort([5,3,2,4,1]))
 

def selection_sort(arr):
    i=0
    while(i<len(arr)):
        min_val=i
        j=i+1
        while(j<len(arr)):
            if arr[j]<arr[min_val]:
              min_val=j
            j+=1
        arr[i],arr[min_val]=arr[min_val],arr[i]
        i+=1
    return arr
print(selection_sort([5,3,2,4,1]))


class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash_func(self,key):
        return key%self.size
    def add(self,key,value):
        index=self.hash_func(key)
        newnode=Node(key,value)
        if self.table[index] is None:
            self.table[index]=newnode
        else:
            temp=self.table[index]
            while(temp.next is not None):
                    temp=temp.next
            temp.next=newnode
    def get(self,key):
        index=self.hash_func(key)
        temp=self.table[index]
        while(temp is not None and temp.key!=key):
            temp=temp.next
        return temp.value
    def dup(self):
        seen=set()
        duplicate=[]
        for i in self.table:
            current=i
            while(current is not None):
                if current.key in seen:
                   duplicate.append(current.key)
                else:
                    seen.add(current.key)
                current=current.next
            return duplicate
    def display(self):
        for i,node in enumerate(self.table):
            print(f"index{i}:",end=" ")
            current=node
            while(current is not None):
                print(f"{current.key}::{current.value}",end="-->")
                current=current.next
            print("none")
table=Hashtable(10)
table.add(10,"move")
table.add(10,"on")
table.add(50,"jaya")
table.add(30,"move")
table.add(40,"on")
table.add(12,"ok ok")
table.add(52,"ok bye")
table.add(59,"ok tk")
table.add(455,"ok koke")
table.display()
print(table.get(30))
print(table.dup())

################################linear prob####################################
class Hashtable:
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
            new_index=(index+i)%self.size
            if self.table[new_index]==key:
                return
    def display(self):
        for i,j in enumerate(self.table):
            print(f"{i}:{j}")
     
table=Hashtable(6)
arr=[1,21,3,40,50]
for i in arr:
    table.add(i)
table.display()

#######################  quick sort ##########################
def quick_sort(arr):
    if len(arr)<1:
        return arr
    else:
        pivot_elem=arr[0]
        less_than=[x for x in arr[1:] if x<pivot_elem]
        greater_than=[x for x in arr[1:] if x>pivot_elem]
        return quick_sort(less_than)+[pivot_elem]+quick_sort(greater_than)
print(quick_sort([3,1,4,2,5]))

#####################  merge sort #########################
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        
        left_half=arr[:mid]
        right_half=arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=j=k=0
        while(i<len(left_half) and j<len(right_half)):
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
print(merge_sort([6,9,8,10,7]))        


######################## stack #############################
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.top=None
    def push(self,key):
        newnode=Node(key)
        seen=set()
        if self.top is None:
            self.top=newnode
        else:
            temp=self.top
            while(temp is not None and temp.key not in seen):
                newnode.next=self.top
                self.top=newnode
    def pop(self):
        if self.top is None:
            return
        popped_data=self.top
        self.top=self.top.next
        return popped_data.data
    def middle_elem(self):
        slow=self.top
        fast=self.top
        prev=None
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
    def pop_spec(self,key):
        temp=self.top
        prev=None
        while(temp is not None and temp.data!=key):
            prev=temp
            temp=temp.next
        prev.next=temp.next

    def display(self):
        if self.top is None:
            print("empty")
        temp=self.top
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        reverse_stack=SlinkedL()
        while self.top is not None:
            reverse_stack.push(self.pop())
        self.top=reverse_stack.top

list=SlinkedL()
arr=[1,2,3,4,5]
for i in arr:
    list.push(i)
list.display()
list.middle_elem()
list.display()
print("reverse")
list.reverse()
list.display()
print("pop")
list.pop()
list.display()
print("pop_spe")
list.pop_spec(4)
list.display()
