#-*- coding:utf-8 -*-
#队列  
class Queue:  
    def __init__(self,size = 16):  
        self.queue = []  
        self.size = size  
        self.front = 0  
        self.rear = 0
    def isEmpty(self):  
        return self.rear == 0  
    def isFull(self):
        # if (self.front - self.rear +1) == self.size:
        if (self.rear - self.front) == self.size:
            return True
        else:  
            return False  
    def popleft(self):
        if self.isEmpty():  
            raise Exception("QueueIsEmpty")  
        else:  
            result = self.queue[self.front]
            del self.queue[self.front]
            self.rear = self.rear - 1
            return result
    def popright(self):
        if self.isEmpty():  
            raise Exception("QueueIsEmpty")  
        else:  
            result =  self.queue[self.rear]
            del self.queue[self.rear]
            self.rear = self.rear - 1
            return result
    def add(self,obj):  
        if self.isFull():  
            raise Exception("QueueOverFlow")  
        else:  
            self.queue.append(obj)  
            self.rear += 1  
    def delete(self):  
        if self.isEmpty():  
            raise Exception("QueueIsEmpty")  
        else:  
            self.rear -=1  
            return self.queue.pop(0)  
    def show(self):  
        print(self.queue)  


q = Queue(3)
q.add(1)
q.add(2)
q.show()
q.delete()
q.show()
