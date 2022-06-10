'''

Author: 小侯
Date: 2022-05-24 08:32:38
LastEditTime: 2022-06-08 09:20:44
LastEditors:    
Description: 
FilePath: \python算法\使用列表\汉偌塔问题.py
'''

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。快速查找
import time

def print_hi(n, a, b, c):
    """

    :param n: 柱子上的盘子数
    :param a: 第一跟柱子
    :param b: 第二根柱子
    :param c: 第三根柱子
    :return:  函数的递归   汉偌塔问题
    """
    # 在下面的代码行中使用断点来调试脚本。
    if n > 0:
        print_hi(n - 1, a, c, b)
        print("把%s移动到%s"%(a, c))
        print_hi(n - 1, b, a, c)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi(4, 'a', 'b', 'c')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
