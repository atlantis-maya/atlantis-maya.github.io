# -*- coding:utf-8 -*-
print("hello python")
print(1+2)
def kp(arr,i,j):    #快排总调用函数
     if i < j:
        base = kpgc(arr,i,j)
        kp(arr,i,base)
        kp(arr,base+1,j)
def kpgc(arr,i,j):    #快排排序过程
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1 #尾指针向后前移动一位
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1 #首指针向后移动一位
            arr[j] = arr[i]
    arr[i] = base
    return i
lst=[1,5,6,8,43,15,68]
kp(lst,0,(len(lst)-1))
print(lst)