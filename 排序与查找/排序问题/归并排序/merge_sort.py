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
    Date: 2022-05-30 10:34:19
LastEditTime: 2022-05-30 14:11:11
LastEditors: your name
    Description: 归并排序   
        思路：将一组无序的列表，通过左节点 右节点还有中间节点进行拆分，
            利用递归地思路---> 将新的列表分为两部分，直到最后剩两个元素的时候不在划分这时候在进行排序
FilePath: \python算法\二叉树的顺序查找\归并排序\merge_sort.py
'''


import random


def merge(ls, left, mid, right):
    #  指向最左边
    i = left
    #  指向右侧区域
    j = mid + 1
    #  存放临时元素
    tem = []
    #  判断左右区域是否有值
    while i <= mid and j <= right:
        # 判断左右区域的开始值得大小，如果右侧大于左侧，那么将左侧的值存放在临时列表里
        if ls[i] < ls[j]:
            tem.append(ls[i])
            i += 1
        else:
            tem.append(ls[j])
            j += 1
            # 具体判断左侧区域的值，也就是剩下最后两个元素的列表得值
    while i <= mid:
        tem.append(ls[i])
        i += 1
        # 具体判断右侧区域的值，也就是剩下最后两个元素的列表得值
    while j <= right:
        tem.append(ls[j])
        j += 1
        # 合并n个列表
    ls[left:right+1] = tem


def merge_sort(ls, left, right):

    if left < right:
        mid = (left + right) // 2

        merge_sort(ls, left, mid)
        merge_sort(ls, mid+1, right)
        merge(ls, left, mid, right)


ls = [i for i in range(50)]
random.shuffle(ls)
print(ls)
merge_sort(ls, 0, len(ls)-1)

print(ls)
