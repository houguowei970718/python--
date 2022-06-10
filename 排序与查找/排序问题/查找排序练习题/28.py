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
Date: 2022-06-06 10:14:15
LastEditTime: 2022-06-06 11:24:10
LastEditors:    
Description: 

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。

    输入: haystack = "hello", needle = "ll"
    输出: 2
FilePath: \python算法\排序方法\查找排序练习题\28.py
'''


from inspect import stack
from sqlalchemy import null


def strStr(haystack, needle):
    j = 0
    stack = []
    h = len(haystack)
    n = len(needle)
# 切片来做
    for i in range(h):
        if haystack[i:n+i] == needle[:]:       
            return i

    # else:
    #     if len(stack) == 0:
    #         return False
    #     elif stack[-1] == haystack[ch]:
    #         i += 1
    #         stack.pop()
    #     else:
    #         return False
    # if len(stack) == 0:
    #     return True
    # for ch in haystack:
    #     if ch in needle:
    #         stack.append[ch]
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         elif stack[-1] == haystack[ch]:
    #             stack.pop()
    #         else:
    #              return False
    # if len(stack) == 0:
    #     return True
    # else:
    #     return False


haystack = "bbbbaaa"
needle = "a"
print(strStr(haystack, needle))
