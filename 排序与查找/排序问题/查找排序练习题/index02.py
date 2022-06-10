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
    Date: 2022-05-30 16:28:46
LastEditTime: 2022-06-01 09:41:04
LastEditors: your name
    Description: 
        编写一个高效的算法来判断 m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
        每行中的整数从左到右按升序排列。
        每行的第一个整数大于前一行的最后一个整数。


FilePath: \python算法\排序方法\查找排序练习题\index02.py
'''

#第一种  采用二分算法 
def find_2d(ls, var):
    M, N = len(ls), len(ls[0])
    left, right = 0, M * N - 1
    while left <= right:
        mid = (right +left) // 2
        # 找出第一个列表的值
        cur = ls[mid // N][mid % N]
        if cur == var:
            return True
        elif cur < var:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 第二种 暴力算法
def index02(list_data,var):
    for i in range(list_data):
        for j in range(list_data):
            if ls[i][j] == var:
                return True
        else:
            return False


ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_data=['abc','defg','hijk','lmn']

index02(list_data, 'h')