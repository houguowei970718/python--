'''
Date: 2022-06-07 09:48:09
LastEditTime: 2022-06-07 15:18:57
LastEditors:    
Description:

    给你一个包含 n 个整数的数组 nums，
    判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
    注意：答案中不可以包含重复的三元组
    输入:nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]


FilePath: \python算法\排序与查找\排序问题\查找排序练习题\15.py
'''


def sum_of_three_numbers(ls):

    n = len(ls)

    temp = []

    ls.sort()
    if n < 3:
        return temp
        # 从最左边开始遍历 n-2表示  除了mid和right
    for left in range(n - 2):
        if ls[left] > 0:
            break

        # if left >= 1 and ls[left] == ls[left-1]:
        #     continue
        mid, right = left + 1, n-1
        # 判断区间是否有值
        while(mid < right):
            if ls[left] + ls[right] + ls[mid] > 0:
                right -= 1
                #  这一步主要 ls[right] == ls[right +1] 判断已经排序好的列表  查找right指针后面的数是否与当前的数重复
                while ls[right] == ls[right + 1] and mid < right:
                    right -= 1
                    #  如果三个数小于零，那么说明已经排序好的列表右边数值小，那么这时候将mid向右移动
            elif ls[left] + ls[right] + ls[mid] < 0:
                mid += 1
                # 当mid+1 的值如果和它前一个数相等  那么跳过去，这时候较少判断的时间，而mid<right就是判断 mid与right之间是否有值
                while ls[mid] == ls[mid - 1] and mid < right:
                    mid += 1
            else:

                # 这个一步就是将合法的值盘序号
                temp.append([ls[left], ls[mid], ls[right]])
                # 向右移动
                mid += 1
                # 向右移动
                right -= 1

                # 当中间数值  小于right的值和他前面是否相等，如果相等或者小于右边的数时，给mid加1，右移一个
                while mid < right and ls[mid] == ls[mid + 1]:
                    mid += 1
                while mid < right and ls[right] == ls[right + 1]:
                    right -= 1

    print(temp)


ls = [-2,0,1,1,2]
sum_of_three_numbers(ls)
