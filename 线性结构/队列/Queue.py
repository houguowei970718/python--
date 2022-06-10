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
Date: 2022-06-06 14:37:08
LastEditTime: 2022-06-07 09:33:05
LastEditors:    
Description: 
        队列是一个数据集合，允许在列表的一端进行插入，另一端进行删除
        进行插入的一段称为队尾(rear)，插入动作称为进队或入队
        进行删除的一端称为队头(front)，删除动作称为出队
        队列的性质：先进先出(first -in ,first-out)


        环形队列   队尾指针 front == MaxSize + 1时，在前进行一个位置自动到
             队首指针前进：front =(front +1) % MaxSize
             队尾指针前进: rear =(rear + )  % MaxSize
             队空条件: rear == front
             队满条件: (rear +1 ) % MaxSize == front

FilePath: \python算法\线性结构\队列\Queue.py
'''

from collections import deque



# 内置队列方法

# def test(size):
#     with open('E:\\python算法\\线性结构\\队列\\123.txt','r') as f:
#         q = deque(f,size)
#         return q
# for line in test(6):
#     print(line,end='')





class Queue:
    def __init__(self, size=100):

        # 默认创建一个队列大小位100
        self.queue=[0 for _ in range(size)]
        self.size =size
        self.rear = 0
        self.front = 0

    # 进队
    def enter_queue(self, element):
        if not self.is_Pull():

            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("队列已经满了")
    # 出队
    def out_queue(self):
        if not self.is_Null():
            self.front=(self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("队列是空")
     
    # 判断队空的条件

    def is_Null(self):
        return self.rear == self.front
            
    # 判断队满

    def is_Pull(self):
        return((self.rear +1 ) % self.size) ==self.front


    def find_first(self):
        pass
    def finf_finall(self):
        pass
queue = Queue(5)

for i in range(4):
    queue.enter_queue(i)


print(queue.out_queue())


queue.enter_queue(4)
