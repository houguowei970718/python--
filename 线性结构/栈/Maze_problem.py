'''

Author: 小侯
Date: 2022-06-06 15:53:42
LastEditTime: 2022-06-07 09:32:39
LastEditors:    

Description: 深度优先算法 

  从指定的一个节点开始，任意找下一个能走的点，
    当找到能走的 这个点时候然后进栈，若碰到不能走的点时候这时 进行出栈（也就是退回上一个点）       
    简单的思想时   找到这个点的路线进栈，不能走的进行出栈
    利用栈的方式取实现（存放路径）
FilePath: \python算法\线性结构\栈\Maze_problem.py
'''


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 上下左右的坐标
dirs = [
    lambda x, y:(x+1, y),
    lambda x, y:(x-1, y),
    lambda x, y:(x, y-1),
    lambda x, y:(x, y+1)
]


def maze_proplem(x1, y1, x2, y2):

    stack = []

    stack.append((x1, y1))

    while (len(stack) > 0):
        # 当前节点
        current_node = stack[-1]
        if current_node[0] == x2 and current_node[1] == y2:
            # 将路径打印出
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            # 查找下一个节点
            nextNode = dir(current_node[0], current_node[1])
            # 如果当前的节点的值等于0说明可以走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                # 如果值等于2说明已经  走过了
                maze[nextNode[0]][nextNode[1]] = 2
                break
                # 若果一个都找不到，那么回退
        else:
            # 标记走过的路
            maze[nextNode[0]][nextNode[1]] = 2
            # 将此时的路出栈
            stack.pop()
    else:
        print("无路可走")
        return False


maze_proplem(1, 1, 8, 8)
