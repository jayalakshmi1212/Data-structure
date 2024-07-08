class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLL:
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
    def sort_list(self):
        if self.head is None or self.head.next is None:
            return
        current = self.head
        while current:
            runner = current.next
            while runner:
                if current.data > runner.data:
                    current.data, runner.data = runner.data, current.data
                runner = runner.next
            current = current.next
                
    def display(self):
        if self.head is None:
            print("linked list is empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        temp=self.head
        prev=None
        while (temp is not None):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev

list=SinglyLL()
arr=[5,2,4,3,1]
for i in arr:
    list.addnode(i)
list.display()
print('sorted')
list.sort_list()
list.display()
        
print("remove middle")
list.remove_middle()
list.display()
print("reverse")
list.reverse()
list.display()
