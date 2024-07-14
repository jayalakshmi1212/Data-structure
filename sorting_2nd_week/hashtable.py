# class Hashtable:
#     def __init__(self,size):
#         self.size=size
#         self.table=[None]*self.size
       
#     def hash_func(self,key):
#         return key%self.size
#     def add(self,key):
#         index=self.hash_func(key)
#         self.table[index]=key
#     def get(self,key):
#         return key%self.size
#     def display(self):
#         print("Key-Value Pairs:")
#         for index,item in enumerate(self.table):
#               print(f"{index} : {item}")
# table=Hashtable(9)
# table.add(10)
# table.add(21)
# table.add(13)
# table.add(34)
# table.add(43)
# table.add(41)
# table.add(45)
# table.display()
# print("get")
# print(table.get(34))
# print(table.get(43))


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
    def display(self):
        for k,v in enumerate(self.table):
            print(f"{k}:{v}")
table=Hash_table(10)
arr=[40,56,78,50,22,34]
for i in arr:
    table.add(i)
table.display()