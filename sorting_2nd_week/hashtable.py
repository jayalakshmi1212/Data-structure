class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
       
    def hash_func(self,key):
        return key%self.size
    def add(self,key):
        index=self.hash_func(key)
        self.table[index]=key
    def get(self,key):
        return key%self.size
    def remove(self,key):
        index=self.hash_func(key)
        if self.table[index]==key:
            self.table[index]=None
            return True
        return False
    def display(self):
        print("Key-Value Pairs:")
        for index,item in enumerate(self.table):
              print(f"{index} : {item}")
table=Hashtable(9)
table.add(10)
table.add(21)
table.add(13)
table.add(34)
table.add(43)
table.add(41)
table.add(45)
table.display()
table.remove(13)
table.display()
print("get")
print(table.get(34))
print(table.get(43))


class Hash_table:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash_func(self,key):
        return key%self.size
    def add(self,key):
        index=self.hash_func(key)
        for i in range(self.size):
            new_index=(index+i)%self.size
            if self.table[new_index] is None:
                self.table[new_index]=key
                return
        print("hash table is full")
    def remove(self,key):
        index=self.hash_func(key)
        for i in range(self.size):
            new_index=(index+i)%self.size
            if self.table[new_index]==key:
                self.table[new_index]=None
                return True
        return False
    def display(self):
        for k,v in enumerate(self.table):
            print(f"{k}:{v}")
table=Hash_table(10)
arr=[40,56,78,50,22,34]
for i in arr:
    table.add(i)
table.display()



##################################### chaining  ####################################

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*self.size
    def hash_func(self,key):
        return key%self.size
    def add(self,key,value):
        index=self.hash_func(key)
        new_node=Node(key,value)
        if self.table[index] is None:
            self.table[index]=new_node
        else:
            temp=self.table[index]
            while(temp.next is not None):
                temp=temp.next
            temp.next=new_node
    def remove(self,key):
        index=self.hash_func(key)
        current=self.table[index]
        prev=None
        while(current is not None):
            if current.key==key:
                if prev is None:
                    self.table[index]=current.next
                else:
                    prev.next=current.next
                return True
            prev=current
            current=current.next
        return False
    def display(self):
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current is not None:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")
table=Hashtable(10)
table.add(10,"chichi")
table.add(20,"dora")
table.add(30,"dorayude preyanem")
table.add(11,"chichi chellumbol")
table.add(12,"nigel")
table.add(16,"varenam")
table.add(19,"chichi dora")
table.display()
table.remove(10)
table.display()
        