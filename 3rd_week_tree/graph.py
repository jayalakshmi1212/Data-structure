from collections import deque

class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex1):
         if vertex1  not  in self.graph:
             self.graph[vertex1]=[]
         
    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1]=[vertex2]
        elif vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if vertex2 not in self.graph:
            self.graph[vertex2]=[vertex1]
        elif vertex1  not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
    
    def remove_vertex(self,vertex):
        if vertex in self.graph:
            connected_verteces=self.graph[vertex]
            del self.graph[vertex]
            for ver in connected_verteces:
                self.graph[ver].remove(vertex)

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def check_if_adjacent(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            return True
        return False
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


    def dfs(self,start):
        visited={v:False for v in self.graph }
        stack=[start]
        result=[]

        while stack:
            vertex=stack.pop()
            if not visited[vertex]:
                visited[vertex]=True
                result.append(vertex)
                stack.extend(reversed(self.graph[vertex]))
        return result
    
    def bfs(self,start):
        visited={v:False for v in self.graph}
        queue=deque([start])
        result=[]

        while queue:
            vertex=queue.popleft()
            if not visited[vertex]:
                visited[vertex]=True
                result.append(vertex)
                queue.extend((self.graph[vertex]))
        return result

gra=Graph()
gra.add_vertex('A')
gra.add_vertex('B')
gra.add_vertex('C')
gra.add_edge('A', 'B')
gra.add_edge('A', 'C')
gra.add_edge('B', 'C')
gra.add_edge('A','D')
gra.display()  
gra.remove_edge('A','B')     
gra.display()
print("DFS:", gra.dfs("A"))
print("BFS:", gra.bfs("A"))