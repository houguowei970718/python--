'''
Author: 小侯
Date: 2022-06-07 16:48:07
LastEditTime: 2022-06-08 16:24:02
LastEditors:    
Description: 
FilePath: \python算法\线性结构\二叉树\binary_tree.py
'''


from inspect import stack
from turtle import left, right


class BinartTree:
    
    def __init__(self, data) -> None:

        self.data = data
        # 左孩子
        self.leftChild = None
        # 右孩子
        self.rightChild = None

        # 先序遍历时  先访问根节点 在遍历左子树，在遍历右子树

    def preTree(self, root):
        if root == None:
            return
        print(root.data)
        self.preTree(root.leftChild)
        self.preTree(root.rightChild)

        # 中序遍历   先遍历左子树，在遍历根节点  再遍历右子树
    def midTree(self, root):
        if root == None:
            return
        self.midTree(root.leftChild)
        print(root.data)
        self.midTree(root.rightChild)

        # 后序遍历   先遍历左子树，  再遍历右子树，在遍历根节点

    def afterTree(self, root):
        if root == None:
            return
        self.afterTree(root.leftChild)
        self.afterTree(root.rightChild)
        print(root.data)

    # 二叉树得节点数目
    def getBinaryTreeSize(self):
        stack = [self.data]
        self.size = 0
        while stack:
            temp = stack.pop(0)
            self.size += 1
            if temp.leftChild:
                stack.append(temp.leftChild)
            if temp.rightChild:
                stack.append(temp.rightChild)
        print(self.size)

    # 二叉树得最大高度
    def getHeight(self, root):
        if not root:
            return 0
        left_deepth = self.getHeight(root.leftChild)
        right_deepth = self.getHeight(root.rightChild)

        return max(left_deepth+1, right_deepth+1)

    # 二叉树得深度
    def getDeepth(self, root):
        return self.getHeight(root)-1


a = BinartTree("A")
b = BinartTree("B")
c = BinartTree("C")

d = BinartTree("D")
e = BinartTree("E")
f = BinartTree("F")
g = BinartTree("G")

e.leftChild = a
e.rightChild = g
a.rightChild = c
g.rightChild = f
c.leftChild = b
c.rightChild = d


root = e

binartTree = BinartTree(root)

# print(root.leftChild.rightChild.data)

# print('\n 先序遍历:',binartTree.preTree(root))


# print('\n 中序遍历:',binartTree.midTree(root))


# print('\n 后序遍历:',binartTree.afterTree(root))

# print('\n 节点数：',)
# print(binartTree.getBinaryTree())


print('\n 二叉树得最大高度:')
print(binartTree.getHeight(root))


print('\n 二叉树得深度:')
print(binartTree.getDeepth(root))
