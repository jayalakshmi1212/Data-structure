###########################################creation of doublylinkedlist and reverse#############################################

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DlinkedL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addnode(self,key):
        newnode=Node(key)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
        self.tail=newnode
    def display(self):
        if self.head is None:
            print("list is empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        if self.head is None:
            return
        temp=self.tail
        while(temp is not None):
            print(temp.data)
            temp=temp.prev
list=DlinkedL()
list.display()
arr=[5,4,3,2,1]
for i in arr:
    list.addnode(i)
list.display()
print("reversed")
list.reverse()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DlinkedL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addnode(self,key):
        newnode=Node(key)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
        self.tail=newnode
    def display(self):
        if self.head is None:
            print("empty list")
        temp=self.tail
        while(temp is not None):
            print(temp.data)
            temp=temp.prev
list=DlinkedL()
list.display()
arr=[1,2,3,4,5]
for i in arr:
    list.addnode(i)
list.display()
        
        
