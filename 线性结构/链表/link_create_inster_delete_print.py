'''
    Author: 小侯
    Date: 2022-06-07 15:36:53
LastEditTime: 2022-06-08 15:03:41
LastEditors:    
    Description: 
FilePath: \python算法\线性结构\链表\link_create_inster_delete_print.py
'''


class line_:
    def __init__(self, item):
        self.item = item
        self.next = None

# 链表的从头部插入值
def create_head(ls):
    # 当前的第一个节点
    head = line_(ls[0])
    # 开始遍历
    for element in ls[1:]:
        # 当前的节点
        current_node = line_(element)
        # 下一个节点的指向前一个的头节点
        current_node.next = head
        # 当前的节点作为头节点
        head = current_node
        # 返回头节点
    return head


# 链表的尾插法
def create_rear(ls):
    # 获取第一个节点
    head = line_(ls[0])
    # 尾节点等于头节点
    rear = head
    for element in ls[1:]:
        # 获取当前的节点
        current_node = line_(element)
        # 当前的节点指向上一个节点得尾节点
        rear.next = current_node
        # 将当前节点得值给尾部连接
        rear = current_node
    return head


ls = [1, 2, 3, 4, 5, 6]
print(ls[-1])
ls = create_rear([1, 2, 3, 4, 5, 6])


def print_ls(ls):
    while ls:
        print(ls.item, end=',')
        ls = ls.next
print_ls(ls)



