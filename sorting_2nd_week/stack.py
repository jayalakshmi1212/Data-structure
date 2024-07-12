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
    def delete_middle(self):
        fast=self.top
        slow=self.top
        prev=None
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
    def remove_even(self):
       
        temp=self.top
        prev=None
        while(temp is not None):
            if temp.data%2==0 :
                 prev.next=temp.next
            else:
                
                prev=temp
            temp=temp.next
    def remove_dup(self):
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
    def pop_specific_elem(self,key):
        temp=self.top
        prev=None
        if temp.data==key:
            self.top=temp.next
            return
        while(temp is not None and temp.data!=key):
            prev=temp
            temp=temp.next
        prev.next=temp.next
    def display(self):
        temp=self.top
        if temp is None:
            print("stack underflow")
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
arr="jayalakshmi"
for i in arr:
    list.push(i)
list.display()
# print("deleted middle")
# list.delete_middle()
# list.display()
# print("pop")
# list.pop()
# list.display()
# print("remove_even")
# list.remove_even()
# list.display()
# print("remove_dup")
# list.remove_dup()
# list.display()
# print("pop_specific_elem")
# list.pop_specific_elem(7)
# list.display()
print("reverse")
list.reverse()
list.display()
        