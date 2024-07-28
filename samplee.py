def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([2,5,3,4,1]))


def push(self,key):
    newnode=Node(key)
    if self.top is None:
        self.top=newnode
    else:
        newnode.next=self.top
        self.top=newnode
def pop(self):
    self.top=self.top.next