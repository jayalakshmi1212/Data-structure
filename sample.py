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
    def remove_middle(self):
        if self.head is None:
            self.head=None
            return
        fast=self.head
        slow=self.head
        prev=None
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
    def display(self):
        if self.head is None:
            print("linked list is empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
list=SlinkedL()
arr=[1,2,3,4,5]
for i in arr:
    list.addnode(i)
list.display()
print("removed middle")
list.remove_middle()
list.display()


def reverse_string(string):
    v=string[::-1]
    return v
print(reverse_string("jaya"))
