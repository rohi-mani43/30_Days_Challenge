class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        new_tail.next = None
        tail.next = head
        
        return new_head
