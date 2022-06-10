'''
 ┌─────────────────────────────────────────────────────────────┐
 │┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐│
 ││Esc│!1 │@2 │#3 │$4 │%5 │^6 │&7 │*8 │(9 │)0 │_- │+= │|\ │`~ ││
 │├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┤│
 ││ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{[ │}] │ BS  ││
 │├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤│
 ││ Ctrl │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  ││
 │├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┬───┤│
 ││ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│Shift │Fn ││
 │└─────┬──┴┬──┴──┬┴───┴───┴───┴───┴───┴──┬┴───┴┬──┴┬─────┴───┘│
 │      │Fn │ Alt │         Space         │ Alt │Win│   HHKB   │
 │      └───┴─────┴───────────────────────┴─────┴───┘          │
 └─────────────────────────────────────────────────────────────┘

    Author: 小侯
    Date: 2022-05-28 11:05:21
LastEditTime: 2022-05-28 16:51:58
LastEditors: your name
    Description: 现在有n个数，设计算法得到前K大的数

    采用堆排序的方式去做
        1、取前k个元素建立一个小根堆。假设堆顶为最大的那个数，然后再依次和剩下列表中的数进行比较，如果比他小，则忽略，如果比他大则替换
        掉此时堆顶元素，那么这时候再根据堆的向下排列的方式对比父节点和孩子节点的大小


FilePath: \python算法\二叉树的顺序查找\堆排序-topk的问题\heap-topk.py
'''
from operator import le
import random
from tkinter import N

def heap_top(ls):
        for i in range(len(ls)-1):
            exchange = False
            for j in range(0, len(ls) - i - 1):
                if ls[j+1] > ls[j]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
                    exchange = True

            if not exchange:
                return ls

def find_k(list_data, k):
        new_list = []
        ls = heap_top(list_data)
        print(ls)
        for i in range(len(ls)):

            if i < k:
                new_list.append(ls[i])

        print(new_list)

list_data = list(range(20))

random.shuffle(list_data)

# print(list_data)
# find_k(list_data, 6)


"""

    采用堆排序的方式去做
        1、取前k个元素建立一个小根堆。假设堆顶为最大的那个数，然后再依次和剩下列表中的数进行比较，如果比他小，则忽略，如果比他大则替换
        掉此时堆顶元素，那么这时候再根据堆的向下排列的方式对比父节点和孩子节点的大小


"""


# 1、 创建一个堆

def create_headp(ls, low, high):
    # low 是指根节点的下标 
    i = low 
    # 开始的左节点
    j = 2 * i + 1
    # 将根节点的值存放在中间变量tem中
    tem = ls[low]
    # 若 孩子节点永远小于数的深度，则一直循环
    while j < high:
        # 若右节点的数小于 深度  并且 右节点小于左节点
        if j + 1 <= high and ls[j+1] < ls[j]:
            # 将他俩的下表交换
            j += 1
        # 如果此时的根节点大于 他的孩子右节点
        if tem > ls[j]:
            # 将此时的右节点的值 赋值给根节点
            ls[i] = ls[j]
            # 然后进行第二层的筛选
            i = j
            # 重新帅选第二的节点
            j = 2 * i + 1
        else:
            break
        ls[i] = tem

# 2、 进行堆排序


def headp_sort_top(ls, k):
    # 取出列表前K个元素，组成一个堆
    heap = ls[0:k]

    for i in range(k-2//2, -1, -1):
        create_headp(heap, i, k-1)

    for i in range(k, len(ls)-1):

        if heap[0] < ls[i]:
            heap[0] = ls[i]
            create_headp(heap, 0, k-1)
    for i in range(k-1, -1, -1):

        heap[0], heap[i] = heap[i], heap[0]

        # i -1 是新的孩子节点

        create_headp(heap, 0, i-1)
    return heap


list_data = list(range(10))

random.shuffle(list_data)

print(headp_sort_top(list_data,8))