# ##################################################### Tree ###########################################################
# class BST:
#     def __init__(self,data):
#         self.data=data
#         self.lchild=None
#         self.rchild=None
    
#     def insert(self,key):
#         if self.data is None:
#             self.data=key
#             return
#         if self.data>key:
#             if self.lchild:
#                 self.lchild.insert(key)
#             else:
#                 self.lchild=BST(key)
#         else:
#             if self.rchild:
#                 self.rchild.insert(key)
#             else:
#                 self.rchild=BST(key)

#     def search(self,key):
#         if self.data==key:
#             print("data found")
#             return
#         if self.data>key:
#             if self.lchild:
#                 self.lchild.search(key)
#             else:
#                 print("data not found")
#         else:
#             if self.rchild:
#                 self.rchild.search(key)
#             else:
#                 print("data not found")
        
#     def delete(self,key):
#         if self.data is None:
#             print("empty")
#         if self.data>key:
#             if self.lchild:
#                 self.lchild=self.lchild.delete(key)
#             else:
#                 print("data is not found cant be delete")
#         elif self.data<key:
#             if self.rchild:
#                 self.rchild=self.rchild.delete(key)
#             else:
#                 print("data is not found cant be delete")
#         else:
#             if self.lchild is None and self.rchild is None:
#                 return
#             if self.lchild is None:
#                 temp=self.rchild
#                 self=None
#                 return temp
#             if self.rchild is None:
#                 temp=self.lchild
#                 self=None
#                 return None
#             node=self.rchild
#             while node.lchild:
#                 node=node.lchild
#             self.data=node.data
#             self.rchild=self.rchild.delete(node.data)

#     def min_val(self):
#         current=self
#         while current.lchild:
#             current=current.lchild
#         return current.data
    
#     def max_val(self):
#         current=self
#         while current.rchild:
#             current=current.rchild
#         return current.data
    
#     def largest(self):
#         current=self
#         while current.rchild:
#             current=current.rchild
#         return current.data
    
#     def smallest(self):
#         current=self
#         while current.lchild:
#             current=current.lchild
#         return current.data
    

#     def preorder(self):
#         print(self.data)
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()
    
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.data)
#         if self.rchild:
#             self.rchild.inorder()
        
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.data)

# root=BST(10)
# arr=[5,20,1,21,3,22]
# for i in arr:
#     root.insert(i)
# root.delete(20)
# root.preorder()
# print(root.max_val())
# print(root.min_val())
# print("heeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaappppppppppppppppppppppppppppp")



# ########################################### heap #####################################

# class max_heap:
#     def __init__(self):
#         self.heap=[]
    
#     def parent_(self,index):
#         return (index-1)//2
    
#     def lchild(self,index):
#         return 2*index+1
    
#     def rchild(self,index):
#         return 2*index+2
    
#     def heapify_up(self,index):
#         parent=self.parent_(index)
#         if index>0 and self.heap[index]>self.heap[parent]:
#             self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
#             self.heapify_up(parent)
    
#     def insert(self,element):
#         self.heap.append(element)
#         self.heapify_up(len(self.heap)-1)

#     def heapify_down(self,index):
#         left=self.lchild(index)
#         right=self.rchild(index)
#         largest=index

#         if left<len(self.heap) and self.heap[left]>self.heap[largest]:
#             largest=left
#         if right<len(self.heap) and self.heap[right]>self.heap[largest]:
#             largest=right
#         if index!=largest:
#             self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
#             self.heapify_down(largest)
    
#     def extract_max(self):
#         if self.heap is None:
#            return None
#         if len(self.heap)==1:
#             return self.heap.pop()
#         root=self.heap[0]
#         self.heap[0]=self.heap.pop()
#         self.heapify_down(0)
#         return root
    
#     def peek_max(self):
#         return self.heap[0] if self.heap else None
    
#     def __str__(self):
#         return str(self.heap)

# mxhp=max_heap()
# arr=[5,2,3,4,1,6]
# for i in arr:
#     mxhp.insert(i)
# print(mxhp)
# print(mxhp.extract_max())
# print(mxhp)





from collections import deque

class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        elif v not in self.graph[u]:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = [u]
        elif u not in self.graph[v]:
            self.graph[v].append(u)

    def remove_vertex(self, v):
        if v in self.graph:
            connected_vertices = self.graph[v]
            del self.graph[v]
            for vertex in connected_vertices:
                self.graph[vertex].remove(v)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def is_adjecent(self,u,v):
        if u in self.graph  and v in self.graph[u]:
            return True
        return False

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs(self, start):
        visited = {v: False for v in self.graph}
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                stack.extend(reversed(self.graph[vertex]))  # Add neighbors to stack

        return result
    
    def bfs(self, start):
        visited = {v: False for v in self.graph}
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                queue.extend(self.graph[vertex])  # Add neighbors to queue

        return result
        
# Example usage
ug = UndirectedGraph()
ug.add_vertex('A')
ug.add_vertex('B')
ug.add_vertex('C')
ug.add_edge('A', 'B')
ug.add_edge('A', 'C')
ug.add_edge('B', 'C')

print("\nUndirected Graph:")
ug.display()
print("DFS:", ug.dfs("A"))
print("BFS:", ug.bfs("A"))
