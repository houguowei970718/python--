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
Date: 2022-05-25 11:05:13
LastEditTime: 2022-06-07 15:13:00
LastEditors:    
Description: 
FilePath: \python算法\排序与查找\排序问题\冒泡，插入，选择排序\sort_list.py
'''

"""
@Project : python算法 
@File : sort_list.py
@Author : Administrator
@Data : 2022/5/25 11:05

列表排序有升序和降序，内置函数有sort（）
排序方式：冒泡排序，选择排序，插入排序


"""
import random





def Bubble_Sort(li):
    """
        冒泡排序：列表每两个相邻的数，如果前面的一个数比后一个数大，则交换位置，
        一趟排序完后，则在无序区减少一个数，有序区增加一个数
    :param list_Data:
    :param var:
    :return:
    """
    # 第几躺
    
    for i in range(len(li) - 1):
        exchange = False
        for j in range(0, len(li) - i - 1):
            """        
                如果前后一个比后一个的数大，则是升序排列            
            """
            if li[j] > li[j + 1]:
                li[j], \
                li[j + 1] = li[j + 1], \
                            li[j]
                exchange = True
        print(li)
        if not exchange:
            return
  


# 选择排序
def selection_sort(list_Data):
    """

    :param list_Data:
    :return: 选择排序  核心点主要是有序区，无序区，查找到无序区最小的数

            1、第一个次记录最小的数，放到第一个位置
            2、第二次在无序区查找最小的数，放到第二个位置
    """
    for i in range(len(list_Data) - 1):
        # 假定第一个数是最小的,这时候再查看后面的数
        mix_index = i
        for j in range(i + 1, len(list_Data)):
            if list_Data[j] < list_Data[mix_index]:
                mix_index = j
                # 判断是否是最后一个数
        if mix_index != i:
            list_Data[j], list_Data[j + 1] = list_Data[j + 1], list_Data[j]
    return list_Data
"""
  插入排序的思路就是，假定第一个数已经排序好了，然后从第二个数开始与第一个数拍好的序列进行对比，
  此时第一个数与第二个数已经安大小排序好了，然后用第三个数与前两个数进行对比，插入到比他前面小的数后面，比他的
  数后面，具体实现就是  从列表小标 1的位置开始对比

"""
        
def insert_sort(list_Data):
    for i in range(1, len(list_Data)):

        j = i - 1

        if list_Data[j] > list_Data[i]:
            
            # 待排序的变量
            temp = list_Data[i]

            print("当前的值:", temp)

            list_Data[i] = list_Data[j]

            j = j - 1

            while j >= 0 and list_Data[j] > temp:
                
                list_Data[j + 1] = list_Data[j]

                j = j - 1

                list_Data[j + 1] = temp



if __name__ == '__main__':
    ls = [9,6,8,5,4,10,2,3,7]
    print(ls)
    selection_sort(ls)
    print(ls)
