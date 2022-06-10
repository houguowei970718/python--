'''
    Description:  快速排序
    Author: 小侯
    Date: 2022-05-25 16:58:16
LastEditTime: 2022-05-26 14:56:43
'''


import random
from pip import main


def partition(ls, left, right):

    # 从左边取第一个数  开始对比
    # random.randint(0,len(ls)-1)
    temp = ls[random.randint(left,len(ls)-1)]
    while left < right:
            # 找出比第一个数小的数  left< right作用是列表的数  是否有相等的数；将其放入到它的左边
        while left < right and ls[right] >= temp:
                # 这里就是循环的意思，让右边的数往回走了一个
            right -= 1
        ls[left] = ls[right]

            # 找出比第一个数大的数  left< right作用是列表的数  是否有相等的数；将其放入到它的右边
        while left < right and ls[left] <= temp:
                eft += 1
        ls[right] = ls[left]
    ls[left] = temp

    print(ls)
    return left


def quick_sort(ls, left, right):

    if left < right:
        key_index = partition(ls, left, right)
        quick_sort(ls, left, key_index-1)
        quick_sort(ls, key_index + 1, right)


ls = [8, 10, 9, 2, 1, 5, 6, 11, 6, 3, 15, 2, 4, 7, 12]


if __name__ == '__main__':
    print(ls)
    quick_sort(ls, 0, len(ls)-1)
    print(ls)
