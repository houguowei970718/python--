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
Date: 2022-05-24 15:07:59
LastEditTime: 2022-06-02 14:29:29
LastEditors:    
Description: 
FilePath: \python算法\排序方法\线性排序\linear_search.py
'''

"""
@Project : python算法 
@File : linear_search.py
@Author : Administrator
@Data : 2022/5/24 15:07
"""

from run_time import run_time

"""

    二分查找必须是一个有序的列表，如果要进行二分查找的话，就必须进行排序。若进行排序了，则时间复杂度就大了，
    如果查找的次数很多就可以使用二分查找，

"""
# 线性查找
@run_time
def linear_search(list_length, var_):
    """

        :param list_length:  列表的长度
        :param var_: 需要查找的值
        :return:  顺序查找
    """
    for i, v in enumerate(list_length):
        if v == var_:
            return i
    else:
        return None


def binary_search(list_length, var_):
    """
        :param list_length:  列表
        :param var_: 查找的值
        :return: mid 需要查找的中间变量的下标
        left: 左下标
        right: 右下标
    """
    left = 0
    i=0
    right = len(list_length) - 1

    # 判断待要查找的区域是否有值
    while left <= right:
        # 中间查找的对比值
        mid = (left + right) // 2
        i += 1
        if list_length[mid] == var_:

            return mid

        elif list_length[mid] > var_:

            right = mid - 1

        else:

            left = mid + 1
    else:

        print("None")

@run_time
def search(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        i = 0 
        right =len(nums) -1
        while left <=right:
            mid  = (left + right) // 2
            i +=1
            if nums[mid] == target:
                return print("%d 出现在 nums 中并且下标为 %d"%(target,mid))
         
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1       
        return  print("%d 不存在 nums 中因此返回 -1"%target)   
            # print("%d 出现在 nums 中并且下标为 %d"%(target,mid))   
      
if __name__ == '__main__':
    nums=[-1,0,3,5,9,12]
    search(1,nums,6)
