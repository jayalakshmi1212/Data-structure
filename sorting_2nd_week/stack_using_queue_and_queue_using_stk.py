
######################### implement stack using quueue ####################################
class Stack:
     def __init__(self):
          self.queue=[]
          self.queue2=[]
     def push(self,element):
          self.queue.append(element)
     def pop(self):
          while(len(self.queue)>1):
               self.queue2.append(self.queue.pop(0))
          popped_element=self.queue.pop(0)
          self.queue,self.queue2=self.queue2,self.queue
          return popped_element
mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3) 
print(mystack.queue)
print(mystack.pop())


################################### implement queue using stack ##################################

class Queue:
     def __init__(self):
          self.stack=[]
          self.stack2=[]
     def enqueue(self,element):
          self.stack.append(element)
     def dequeue(self):
          if not self.stack2:
               while(self.stack):
                    self.stack2.append(self.stack.pop())
          return self.stack2.pop()
     def peek(self):
          if not self.stack2:
               while(self.stack):
                    self.stack2.append(self.stack.pop())
          return self.stack2[-1]
myqueue=Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue.stack)
myqueue.dequeue()
print(myqueue.stack2)
print(myqueue.peek())
               

