# Linked List
# Time Complexity: O(n) / 71ms(5.19%)
class ListNode():
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.space = k
        self.head = ListNode(0, None, None)
        self.tail = ListNode(0, None, self.head)
        self.head.next = self.tail

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            new = ListNode(value, self.tail, self.tail.prev)
            self.tail.prev.next = new
            self.tail.prev = new
            self.space -= 1
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.space += 1
            return True


    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.head.next == self.tail :
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
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()