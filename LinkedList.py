class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node(0)  # sentinel (dummy head)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):  # move index+1 times from sentinel
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        if index > self.size:
            return

        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        newNode = Node(val)
        newNode.next = pred.next
        pred.next = newNode

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next


# Example usage:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)   # linked list becomes 1->2->3
# print(obj.get(1))      # returns 2
# obj.deleteAtIndex(1)   # now the list is 1->3
# print(obj.get(1))      # returns 3
