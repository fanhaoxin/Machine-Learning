# coding:utf-8

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList(object):
        def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        cnt = 0
        while cur != None:
            cnt = cnt + 1
            cur = cur.next
        return cnt

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node
            node.next.prev = node


    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            cnt = 0
            while cnt != pos:
                cnt = cnt + 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                    cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
                
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item :
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()

