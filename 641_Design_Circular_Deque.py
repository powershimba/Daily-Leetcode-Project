# 641. Design Circular Dequeue (Medium)

# Linked List
# Time Complexity: O(n) / 67ms(7.86%)
# Memory Complexity: O(n) / 14.42MB(5.62%)

class ListNode():
    def __init__(self, value, nxt, prev):
        self.val, self.next, self.prev = value, nxt, prev

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.space = k
        self.head = ListNode(None, None, None)
        self.tail = ListNode(None, None, self.head)
        self.head.next = self.tail

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.new = ListNode(value, self.head.next, self.head)
        self.head.next.prev = self.new
        self.head.next = self.new
        self.space -= 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.new = ListNode(value, self.tail, self.tail.prev)
        self.tail.prev.next = self.new
        self.tail.prev = self.new
        self.space -= 1
        return True        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.space += 1
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.space += 1
        return True
        
    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.next.val        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.head.next == self.tail:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.space == 0:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()