class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.count = 0

        self.sentinel = Node(0,0)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        self.moveFirst(self.nodeMap[key])
        return self.nodeMap[key].val

    def addFirst(self, key, val):
        old_first = self.sentinel.next

        node = Node(
            key,
            val,
            self.sentinel,
            old_first
        )

        self.sentinel.next = node
        old_first.prev = node

        self.nodeMap[key] = node
        self.count += 1

    def moveFirst(self, node):
        oldP = node.prev
        oldN = node.next
        oldP.next = oldN
        oldN.prev = oldP
        oldFirst = self.sentinel.next
        self.sentinel.next = node
        node.prev = self.sentinel
        node.next = oldFirst
        oldFirst.prev = node
    
    def removeLast(self):
        cut = self.sentinel.prev
        old = cut.prev
        self.sentinel.prev = old
        old.next = self.sentinel
        cut.prev, cut.next = None, None
        del self.nodeMap[cut.key]
        self.count -= 1

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap:
            self.addFirst(key, value)
        else:
            self.moveFirst(self.nodeMap[key])
            self.sentinel.next.val = value
        if self.capacity < self.count:
            self.removeLast()
            
        

        
