class BST:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.Rightchild=None
    def insert(self,data):
        if self.data is None:
            self.data=data
            return
        if self.data==data:
            return
        if self.data>data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild=BST(data)
        else:
            if self.Rightchild:
                self.Rightchild.insert(data)
            else:
                self.Rightchild=BST(data)


##################################                    serach                  ###############################
class BST:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.leftchild:
                self.leftchild.insert(key)
            else:
                self.leftchild=BST(key)
        else:
            if self.rightchild:
                self.rightchild.insert(key)
            else:
                self.rightchild=BST(key)

    def search(self,key):
        if self.data==key:
            print("node found")
            return
        if self.data>key:
            if self.leftchild:
                self.leftchild.search(key)
            else:
                print("node not found")
        else:
            if self.rightchild:
                self.rightchild.search(key)
            else:
                print("node not found")

root=BST(20)
arr=[10,30,50,5,20]
for i in arr:
    root.insert(i)
root.search(300)

###############################                 traversal                          #####################

###############################                 preorder                           #####################

class BST:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightC=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.leftc:
                self.leftc.insert(key)
            else:
                self.leftc=BST(key)
        else:
            if self.rightC:
                self.rightC.insert(key)
            else:
                self.rightC=BST(key)
    def search(self,key):
        if self.data==key:
            print("data found")
            return
        if self.data>key:
            if self.leftc:
                self.leftc.search(key)
            else:
                print("not found")
        else:
            if self.rightC:
                self.rightC.search(key)
            else:
                print("not found")
    def preorder(self):
        print(self.data)
        if self.leftc:
            self.leftc.preorder()
        if self.rightC:
            self.rightC.preorder()

root=BST(None)
arr=[5,1,2,0,3,6,7,4]
for i in arr:
    root.insert(i)
root.preorder()
root.search(5)


#########################################in and pre order#############################################

class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.lchild:
               self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    def search(self,key):
        if self.data==key:
            print("data found")
            return
        if self.data>key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("not found")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("not found")
    def preorder(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data,end=" ")
root=BST(20)
arr=[50,40,10,5,60,4,15]
for i in arr:
    root.insert(i)
print("preorder")
root.preorder()
print("\ninorder")
root.inorder()
print("\npostorder")
root.postorder()

########################################## delete #########################################

class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    def search(self,key):
        if self.data==key:
            print("data found")
            return
        if self.data>key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("data not found")
        else:
            if self.data<key:
                if self.rchild:
                    self.rchild.search(key)
                else:
                    print("data not found")
    
    def delete(self,key):
        if self.data is None:
            print("tree is empty")
            return 
        if self.data>key:
            if self.lchild:
                self.lchild=self.lchild.delete(key)
            else:
                print("data is not in the key")
        elif self.data<key:
            if self.rchild:
                self.rchild=self.rchild.delete(key)
            else:
                print("data is not in the key")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(node.data)
        return self
              
    def preorder(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)
def delete_root(root, key):
    if root is None:
        return None
    return root.delete(key)

root=BST(None)    
arr=[30,20,90]
for i in arr:
    root.insert(i)
root=delete_root(root,30)
root.delete(30)
print("\nInorder traversal after deletion:")
root.inorder()



#########################################    min and max ########################################

class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data==key:
            return
        if self.data>key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    def search(self,key):
        if self.data==key:
            print("data found")
            return
        if self.data>key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("data not found")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("data not found")
    def delete(self,key):
        if self.data is None:
            print("empty")
            return
        if self.data>key:
            if self.lchild:
                self.lchild=self.lchild.delete(key)
            else:
                print("node not found in the tree")
        elif self.data<key:
            if self.rchild:
                self.rchild=self.rchild.delete(key)
            else:
                print("node not found in the tree")
        else:
            if self.lchild is None and self.rchild is None:
                return
            if self.lchild is None:
                temp=self.rchild
                return temp
            if self.rchild is None:
                temp=self.lchild
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(node.data)
        return self
    def min_value(self):
        current=self
        while current.lchild:
            current=current.lchild
        return current.data
        
    def max_value(self):
        current=self
        while current.rchild:
            current=current.rchild
        return current.data
      
    def preorder(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)

def root_delete(root, key):
    if root is None:
        return None
    return root.delete(key)


root=BST(10)
arr=[1,5,20]
for i in arr:
    root.insert(i)
root.delete(5)
root=root_delete(root,10)
if root:
    root.preorder()
else:
    print("Tree is empty after deletion of the root node")

print("\n")

print("Minimum value in the BST:")
print(root.min_value())

print("Maximum value in the BST:")
print(root.max_value())
        



###############################################################################################################################

class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,key):
        if self.data is None:
            self.data=key
            return
        if self.data>key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild=BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild=BST(key)
    def search(self,key):
        if self.data==key:
            print("data found")
            return
        if self.data>key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("data not found")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("data not found")
    def delete(self,key):
        if self.data is None:
            print("empty")
            return
        if self.data>key:
            if self.lchild:
                self.lchild=self.lchild.delete(key)
            else:
                print("node not found")
        elif self.data<key:
            if self.rchild:
                self.rchild=self.rchild.delete(key)
            else:
                print("node not found")
        else:
            if self.lchild is None and self.rchild is None:
                 return
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(node.data)
        return self
    def min_val(self):
        current=self
        while current.lchild:
            current=current.lchild
        return current.data
    def max_val(self):
        current=self
        while current.rchild:
            current=current.rchild
        return current.data
    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)
print("####################################################################################")
root=BST(10)
arr=[1,2,12,3]
for i in arr:
    root.insert(i)
root.delete(2)
if root:
   root.preorder()
else:
    print("it is not containing the value")
print("max val:")
print(root.max_val())
print("min_val:")
print(root.min_val())