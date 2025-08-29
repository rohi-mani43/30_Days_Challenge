class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [0] * k
        self.size = k
        self.count = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
