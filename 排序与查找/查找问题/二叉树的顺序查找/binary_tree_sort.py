'''
    Author: 小侯
    Date: 2022-05-26 16:18:30
LastEditTime: 2022-05-30 11:11:14
LastEditors: your name
    Description:
    
        堆排序----一种特殊的完全二叉树结构
                大根堆: 一个完全二叉树，满足任一节点都比其他孩子节点大   排出来的是升序列表
                小根堆：一个完全二叉树，满足任一节点都比其他孩子节点小   排出来的是降序列表

FilePath: \python算法\二叉树的顺序查找\binary_tree_sort.py
'''


'''
        description:  创建堆
        param {*} ls 传入的列表
        param {*} low 堆根节点的位置
        param {*} high 堆的最后一个元素的位置
        return {*}
    '''

import random
import time

import heapq

def create_heap(ls, low, high):
    i = low   # 变量i 是指开始的根节点

    j = i * 2 + 1  # j孩子节点的从左开始

    tmp = ls[low]  # 把堆的节点存起来

    while j <= high:  # 开始的左节点是否在最后一个节点之前

        if j + 1 <= high and ls[j+1] > ls[j]:

            j = j + 1  # 这时候将j 调节成右孩子

        if ls[j] > tmp:  # 此时判断当前的根节点的数 与孩子节点比较

            ls[i] = ls[j]

            i = j  # 此时第一层已经判断完成，然后将i往下一层转换，然后j也想下移动

            j = i * 2 + 1  
        else:
            ls[i] = tmp  # 把tmp放到某一级父节点的位置上
            break
    else:
        ls[i] = tmp
    # 堆排序  从小到大

def head_sort(list_Data):

    n = len(list_Data)
    st_time = time.time()

    # todo  从最后一个父节点与她的孩节点进行最小堆处理，判断  父节点与孩节点的大小值 归并排序
    for i in range((n-2)//2, -1, -1):

        # i 表示建堆的时候调整的部分的跟下表
        create_heap(list_Data, i,  n-1)

    for i in range(n-1, -1, -1):

        list_Data[0], list_Data[i] = list_Data[i], list_Data[0]
        # i -1 是新的孩子节点
        create_heap(list_Data, 0, i-1)
    sp_time = time.time()


    print("runing time: %s secs." %(sp_time - st_time))



ls = [i for i in range(10)]
random.shuffle(ls)
print(ls)
head_sort(ls)
print(ls)
