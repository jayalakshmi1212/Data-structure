# # ############################################create a node and add node###############################################


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Singlelinkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addNode(self,key):
#         newNode=Node(key)
#         if self.head is None:
#             self.head=newNode
#         else:
#             self.tail.next=newNode
#         self.tail=newNode
#     def display(self):
#         if self.head is None:
#             print("empty")
#             return
#         temp=self.head
#         while temp is not None:
#             print(temp.data)
#             temp=temp.next
# list=Singlelinkedlist()
# list.display()
# # a=[10,20,30,40]
# # for i in a:
# #     list.addNode(i)
# # list.display()
# list.addNode(10)
# list.addNode(50)
# list.addNode(100)
# list.addNode(150)
# list.display()


# ############################################################insertion of node########################################################


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class slinkedl:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addNode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#              self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def insertbeginning(self,key):
#         newnode=Node(key)
#         newnode.next=self.head
#         self.head=newnode
#     def insertafter(self,nexto,key):
#         newnode=Node(key)
#         temp=self.head
#         while(temp is not None and temp.data!=nexto):
#             temp=temp.next
#         if self.tail==nexto:
#             self.tail.next=newnode
#             self.tail=newnode
#             return
#         newnode.next=temp.next
#         temp.next=newnode
#     def insertend(self,key):
#         newnode=Node(key)
#         self.tail.next=newnode
#         self.tail=newnode
#     def display(self):
#         if self.head is None:
#             print("linked list is empty")
#             return
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
# list=slinkedl()
# list.addNode(40)
# list.addNode(50)
# list.addNode(60)
# list.addNode(70)
# list.display()
# print("insertbeginning")
# list.insertbeginning(30)
# list.display()
# print('insetafter')
# list.insertafter(50,10)
# list.insertend(20)
# list.display()


 ###################################################deletion of a node##################################################


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def deleteafter(self,key):
#         temp=self.head
#         prev=None
#         if temp.data==key:
#             self.head=temp.next
#             return
#         while(temp is not None and temp.data!=key):
#             prev=temp
#             temp=temp.next
#         if temp is None:
#             return
#         if temp==self.tail:
#             self.tail=prev
#             self.tail.next=None
#             return
#         prev.next=temp.next

#     def display(self):
#         if self.head is None:
#             print("linked list is empty")
#             return
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
# list=SlinkedL()
# list.display()
# arr=[40,50,60,20,70,80]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("delete after")
# list.deleteafter(80)
# list.display()
               
        

#######################################remove duplicate#############################################


# class Node:
#     def __init__(self,data) :
#         self.data=data
#         self.next=None
# class slinkedl:
#     def __init__(self) :
#         self.head=None
#         self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def removeduplicates(self):
#         if self.head is None:
#             return
#         values=set()
#         temp=self.head
#         prev=None
#         while(temp is not None):
#             if temp.data  in values:
#                 prev.next=temp.next
#             else:
#                 values.add(temp.data)
#                 prev=temp
#             temp=temp.next

#     def display(self):
#         if self.head is None:
#             print("linked list is empty")
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next
# list=slinkedl()
# list.display()
# arr=[10,20,30,20,50,50,50,70,70]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("removed duplicate number in the list")
# list.removeduplicates()
# list.display()



##############################################delete evennumbers###############################################

# class Node:
#     def __init__(self,data) :
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def del_evennumbers(self):
#         if self.head is None:
#             return
#         values=set()
#         temp=self.head
#         prev=None
#         while(temp is not None):
#             if temp.data%2==0:
#                 prev.next=temp.next
#             else:
#                 values.add(temp.data)
#                 prev=temp
#             temp=temp.next
#     def display(self):
#         if self.head is None:
#             print("empty list")
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next

# list=SlinkedL()
# list.display()
# arr=[1,2,3,4,5]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("del_even")
# list.del_evennumbers()
# list.display()
        
        

#####################################delete middle##########################################################


# class Node:
#     def __init__(self,data) :
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode
#     def delete_middle(self):
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
#         if prev is not None:
#             prev.next=slow.next

#     def display(self):
#         if self.head is None:
#             print("empty list")
#         temp=self.head
#         while(temp is not None):
#             print(temp.data)
#             temp=temp.next

# list=SlinkedL()
# list.display()
# arr=[1,2,3,4,5]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("del_mid")
# list.delete_middle()
# list.display()
        

##################################################reverse###########################################


# class Node:
#     def __init__(self,data) :
#         self.data=data
#         self.next=None
# class SlinkedL:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addnode(self,key):
#         newnode=Node(key)
#         if self.head is None:
#             self.head=newnode
#         else:
#             self.tail.next=newnode
#         self.tail=newnode

#     def display(self):
#         if self.head is None:
#             print("empty list")
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
# list.display()
# arr=[1,2,3,4,5]
# for i in arr:
#     list.addnode(i)
# list.display()
# print("reversed list")

# list.reverse()
# list.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addnode(self,key):
        newnode=Node(key)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def insertbeginning(self,key):
        newnode=Node(key)
        newnode.next=self.head
        self.head=newnode
    def insertafter(self,nexto,key):
        newnode=Node(key)
        temp=self.head
        if self.head is None:
            return
        
        while(temp is not None and temp.data!=nexto):
            temp=temp.next
        if self.tail==nexto:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=None
            return
        newnode.next=temp.next
        temp.next=newnode
    def insertend(self,key):
        newnode=Node(key)
        self.tail.next=newnode
        self.tail=newnode
        self.tail.next=None
    def delete(self,key):
        temp=self.head
        prev=None
        if temp.data==key:
            temp=temp.next
            return
        while(temp is not None and temp.data!=key):
            prev=temp
            temp=temp.next
        if temp is None:
            return
        if temp==self.tail:
            self.tail=prev
            self.tail.next=None
        prev.next=temp.next
    def remove_duplicates(self):
        if self.head is None:
            return
        values=set()
        temp=self.head
        prev=None
        while(temp is not None):
            if temp.data in values:
                prev.next=temp.next
            else:
                values.add(temp.data)
                prev=temp
            temp=temp.next
    def remove_even(self):
        if self.head is None:
            return
        values=set()
        temp=self.head
        prev=None
        while(temp is not None):
            if temp.data %2==0 :
                if temp is None:
                    prev.next=temp.next
                else:
                    values.add(temp.data)
                    prev=temp
            temp=temp.next

            
    def display(self):
        if self.head is None:
            print("list is empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
list=SlinkedL()
arr=[1,2,3,4,5,4,5]
for i in arr:
    list.addnode(i)
list.insertbeginning(6)
list.insertafter(3,7)
list.insertend(10)
list.delete(2)
list.remove_duplicates()
list.remove_even()
list.display()



        

        