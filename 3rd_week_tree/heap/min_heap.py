class min_heap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)//2
    
    def left_child(self,index):
        return 2*index+1
    
    def right_child(self,index):
        return 2*index+2
    
    def heapify_up(self,index):
         parent=self.parent(index)
         if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
    
    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self,index):
        left=self.left_child(index)
        right=self.right_child(index)
        smallest=index

        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if index!=smallest:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapify_down(smallest)

    def extract_min(self):
        if self.heap is None:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    
    def peek_min(self):
        return self.heap[0] if self.heap else None
    
    def __str__(self):
        return str(self.heap)

minhp=min_heap()
arr=[5,4,9,7,2,1]
for i in arr:
    minhp.insert(i)
print(minhp)
print(minhp.extract_min())
print(minhp)
print(minhp.peek_min())
