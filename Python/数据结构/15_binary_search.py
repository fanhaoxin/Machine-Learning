# coding:utf-8

def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        elif item > alist[mid]:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_2(alist, item):
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        elif item > alist[mid]:
            first = mid + 1
    return False

if __name__ == "__main__":
    li = [17, 20, 31, 44, 54, 55, 77, 93, 226]
    print(li)
    print(binary_search(li, 55))
    print(binary_search(li, 100))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))


    