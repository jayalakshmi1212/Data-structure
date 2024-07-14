class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,key):
        newnode=Node(key)
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
print("dequeue")
list.dequeue()
list.display()