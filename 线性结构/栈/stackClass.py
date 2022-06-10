'''

    Author: 小侯

    Date: 2022-06-01 14:56:13

LastEditTime: 2022-06-08 09:23:12

LastEditors:    

    Description:  栈的 出近问题     括号匹配

FilePath: \python算法\线性结构\栈\stackClass.py


'''


class Stack:
    def __init__(self):
        self.stack = []

    # 出栈  out_of_stack
    def out_of_stack(self):
        
        return self.stack.pop()

    def enter_stack(self, element):

        self.stack.append(element)

    def get_top(self):

        if len(self.stack) > 0:

            return self.stack[-1]
        else:

            return None

    def is_empty(self):

        return len(self.stack) == 0

def brace_match(s):

    stack = Stack()

    match = {')': '(', '}': '{', ']':'['}

    for ch in s:

        if ch in {'(', '[', '{'}:

            stack.enter_stack(ch)

        else:

            if stack.is_empty():

                return False

            elif stack.get_top() == match[ch]:

                stack.out_of_stack()

            else:  # stack.enter_stack(ch)

                return False

    if stack.is_empty():

        return True

    else:
        return False

print(brace_match('[]'))

print(brace_match('()'))