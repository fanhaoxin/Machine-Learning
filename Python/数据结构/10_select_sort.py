# coding : utf-8

alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]

def select_sort(alist):
    for j in range(len(alist)-1):
        min_index = j
        for i in range(j+1, len(alist)):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

print(alist)
select_sort(alist)
print(alist)