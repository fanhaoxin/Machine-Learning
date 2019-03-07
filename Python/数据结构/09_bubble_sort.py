# coding : utf-8

def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

if __name__ == "__main__":
    li = [3,4,1,1,4,6,8,3]
    print(li)
    bubble_sort(li)
    print(li)