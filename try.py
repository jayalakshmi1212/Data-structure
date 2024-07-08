class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SlinkedL:
    def __init__(self) :
         self.head=None
         self.tail=None
    def addnode(self,key):
        newnode=Node(key)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def insertbeg(self,key):
        newnode=Node(key)
        newnode.next=self.head
        self.head=newnode
    def insaft(self,nexto,key):
        newnode=Node(key)
        temp=self.head
        prev=None
        while(temp is not None and temp.data!=nexto):
            temp=temp.next
        if self.tail==nexto:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=None
        newnode.next=temp.next
        temp.next=newnode
    def delete(self,key):
        temp=self.head
        prev=None
        if(temp.data==key):
            self.head=temp.next
            return
        while(temp is not None and temp.data!=key):
            prev=temp
            temp=temp.next
        if temp is None:
            return
        if(temp==self.tail):
            self.tail=prev
            self.tail.next=None
            return
        prev.next=temp.next
    def middle(self):
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
            print("list is empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        temp=self.head
        prev=None
        while(temp is not None):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
list=SlinkedL()
arr=[1,2,3,4,5,6]
for i in arr:
    list.addnode(i)
list.display()
print("inb")
list.insertbeg(3)
list.display()
print('blaaaaaaaaaaaaa')
list.insaft(4,7)
list.display()
print("laaaaaaaaaaaaaaaaa")
list.delete(7)
list.display()
print("klaaaaaaaaaaa")
list.reverse()
list.display()
print("klee")
list.middle()
list.display()

print("biiii")
def binary_search(arr,target):
    left,right=0,len(arr)
    mid=left+right//2
    while(left<=right):
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
print(binary_search([1,2,3,4,5],3))


def palindrome(arr):
    if len(arr)<=1:
        return True
    if arr[0]!=arr[-1]:
        return False
    return palindrome(arr[1:-1])
print(palindrome("racecar"))

def factorial(arr):
    if arr<=1:
       return 1
    return arr*factorial(arr-1)
print(factorial(5))

def sum(arr):
    if not arr:
        return 0
    return arr[0]+sum(arr[1:])
print(sum([1,2,3,4,5]))