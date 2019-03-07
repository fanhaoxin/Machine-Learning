# coding:utf-8

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

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

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self._head
            cnt = 0
            while cnt != pos-1:
                cnt = cnt + 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        pre = self._head
        while pre.next.elem != item:
            pre = pre.next
        pre.next = pre.next.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item :
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
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