# Chaining
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if node is empty, put the pair
        i = key % self.size
        if self.table[i].value == None: # Not `table[i] == None`
            self.table[i] = ListNode(key, value)
            return

        # if node is not empty, search next space
        p = self.table[i]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        i = key % self.size
        if self.table[i].value is None:
            return -1
        p = self.table[i]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % self.size
        if self.table[i].value is None:
            return
        p = self.table[i]

        # if first node is target
        if p.key == key:
            if p.next is None:
                self.table[i] = ListNode()
            else:
                self.table[i] = p.next
            return
        # else
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
            
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)