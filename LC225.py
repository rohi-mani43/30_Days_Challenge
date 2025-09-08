from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        # rotate so that last pushed element comes to front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q


# Example usage:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())    # 2
# print(obj.pop())    # 2
# print(obj.empty())  # False
