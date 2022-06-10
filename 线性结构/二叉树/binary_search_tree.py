from lib2to3.pytree import Node
from logging import root
import random


class BinartTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent_Node = None


class BinartSearchTree:
    def __init__(self, ls=None):
        self.root = None
        if ls:
            for val in ls:
                self.ord_insert(val)
    # 递归写法

    def insert_val(self, node, val):
        if not node:
            node = BinartTree(val)
        elif val < node.data:
            node.left_child = self.insert_val(node.left_child, val)
            node.left_child.parent_Node = node
        elif val > node.data:
            node.right_child = self.insert_val(node.right_child, val)
            node.right_child.parent_Node = node
        return node

    # 非递归
    def ord_insert(self, val):
        # 拿到当前根节点
        root = self.root
        if root is None:
            # 当根节点是空得话，将值直接赋值得根节点
            self.root = BinartTree(val)
            return
        while True:
            # 如果当前的值小于 根节点得值
            if val < root.data:
                # 如果当前根节点有左孩子
                if root.left_child:
                    # 将当前得左子树得  指向root
                    root = root.left_child
                else:  # 左孩子不存在 将当前的值放在此时的根节点的左孩子上
                    root.left_child = BinartTree(val)
                    root.left_child.parent_Node = root
            elif val > root.data:
                if root.right_child:
                    root = root.right_child
                else:
                    root.right_child = BinartTree(val)
                    root.right_child.parent_Node = root
                    return
            else:
                return

    # 先序遍历时  先访问根节点 在遍历左子树，在遍历右子树
    def preTree(self, root):
        if root:
            print(root.data, end=',')
            self.preTree(root.left_child)
            self.preTree(root.right_child)

    # 中序遍历   先遍历左子树，在遍历根节点  再遍历右子树
    def midTree(self, root):
        if root:
            self.midTree(root.left_child)
            print(root.data, end=',')
            self.midTree(root.right_child)

     # 后序遍历   先遍历左子树，  再遍历右子树，在遍历根节点
    def afterTree(self, root):
        if root:

            self.afterTree(root.left_child)
            self.afterTree(root.right_child)
            print(root.data, end=',')

    # 查询
    def search(self, val):
        # 指向根节点
        root = self.root
        # 如果一直有根节点
        while root:
            # 如果此时节点的值 小于查询的值
            if root.data < val:
                # 那么从右子树中查询
                root = root.right_child
            elif root.data > val:
                root = root.left_child
            else:
                return root
    # 第一种情况是  没有孩子节点的情况

    def delete_one_case(self, node):
        # 判断是否是空树
        if node.parent_Node is None:
            self.root = node

        # 判断这个节点是在左孩子上还是右孩子
        if node.parent_Node.left_child == node:
            node.parent_Node.left_child = None
        else:
            node.parent_Node.right_child = None
    # 第二种是只有一个右孩子或者左孩子

    def delete_two_case(self, node):

        # 判断此时的根节点是否为空
        if node.parent_Node is None:
            # 如果是空 直接将此时节点的左孩子的值  给 root根节点
            self.root = node.left_child
            # 那么此时  该节点的左孩子的父亲节点就是None
            node.left_child.parent_Node = None
        # 如果根节点不是空  并且此时的节点是它父亲的的左孩子
        elif node == node.parent_Node.left_child:
            # 那么将此时节点的左孩子的值  和  它父亲的左孩子的值连接起来，也就是替换
            node.parent_Node.left_child = node.left_child
            # 则此时的节点的父亲节点 的值和左孩子的父亲节点的值连起来
            node.left_child.parent_Node = node.parent_Node
        else:

            node.parent_Node.right_child = node.right_child
            node.right_child.parent_Node = node.parent_Node

    def delete(self, val):
        if self.root:
            node = self.search(val)
            if not node:
                raise IndexError("没有此值")
            # 第一种情况  没左孩子和右孩子
            if not node.left_child and not node.right_child:
                self.delete_one_case(node)
                #  第二种情况 没有右孩子的情况就只有左孩子
            elif not node.right_child:
                self.delete_two_case(node)
                # 第二种情况 没有左孩子情况就只有右孩子
            elif not node.left_child:
                self.delete_two_case(node)
            else:
                # 先找出右子树
                mix_node = node.right_child
                # 如果此节点只有左孩子的情况下
                while mix_node.left_child:
                    # 那么将此节点的左孩子 作为这个最小的值得节点
                    mix_node = mix_node.left_child
                    # 然后获取到此节点得值 并且赋值给当前得结点得值
                    node.data = mix_node.data
                    # 如果这个做小的节点有右孩子
                if mix_node.right_child:
                    # 调用第二种情况得函数？（只有一右孩子或者左孩子得情况）
                    self.delete_two_case(mix_node)
                else:
                    self.delete_one_case(mix_node)


class BinartSearchTree2:
    def __init__(self) -> None:

        self.root = None

    # 先序 访问根节点---->左子树----->右子树
    def preorder(self, root):
        if root:
            print(root.data, end=",")
            self.preorder(root.left_child)
            self.preorder(root.right_child)
    # 中序 先左子树---->根节点---->右子树

    def MiddleOrder(self, root):
        if root:
            self.MiddleOrder(root.left_child)
            print(root.data, end=",")
            self.MiddleOrder(root.right_child)
    # 后序  先左子树  ---->右子树---->根节点

    def Afterword(self, root):
        if root:
            self.preorder(root.left_child)
            self.preorder(root.right_child)
            print(root.data, end=",")

    # 查询节点
    def QueryNode(self, val):
        if self.root is None:
            return
        while self.root:
            if self.root.data < val:
                self.QueryNode(self.root.right_child, val)
            elif self.root.data > val:
                self.QueryNode(self.root.left_child, val)
            else:
                return self.root
    

li = [17, 5, 35, 2, 11, 29, 38, 9, 16, 8]


tree = BinartSearchTree(li)
# print("中序\n")
# tree.midTree(tree.root)
tree.midTree(tree.root)
print(" ")

tree.delete(5)
tree.delete(2)
tree.midTree(tree.root)
