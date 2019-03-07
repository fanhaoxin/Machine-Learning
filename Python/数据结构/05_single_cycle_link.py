# coding:utf-8

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        cnt = 1
        while cur.next != self._head:
            cnt = cnt + 1
            cur = cur.next
        return cnt

    def travel(self):
        if self.is_empty():
            return None
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.next = self._head
    
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
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                if cur == self._head:
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    rear.next = cur.next
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self._head:
                self._head = None
            else:
                pre.next = cur.next



    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item :
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.add(2)
    ll.add(3)
    ll.add(4)

    ll.travel()
    ll.insert(2, 8)
    ll.travel()
    print(ll.search(000))
    ll.remove(8)
    ll.travel()