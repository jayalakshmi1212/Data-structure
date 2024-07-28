class max_heap:
    def __init__(self):
        self.heap=[]

    def _parent(self,index):
        return (index-1)//2
    
    def left_child(self,index):
        return 2*index+1
    
    def right_child(self,index):
        return 2*index+2
    
    def  heapify_up(self,index):
        parent=self._parent(index)
        if index>0 and self.heap[index]>self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
    
    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)

    def heapify_down(self,index):
        left=self.left_child(index)
        right=self.right_child(index)
        largest=index

        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if index!=largest:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self.heapify_down(largest)

    def extract_max(self):
        if self.heap is None:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    
    def peek_max(self):
        return self.heap[0] if self.heap else None
    
    def __str__(self):
        return str(self.heap)
    
maxhp=max_heap()
maxhp.insert(10)
maxhp.insert(5)
maxhp.insert(2)
maxhp.insert(3)
maxhp.insert(20)
print(maxhp)
print(maxhp.extract_max())
print(maxhp)
print(maxhp.peek_max())


