'''
    Author: 小侯
    Date: 2022-05-24 08:33:26
LastEditTime: 2022-06-08 15:03:52
LastEditors:    
    Description: 
FilePath: \python算法\使用列表\__init__.py
'''

def uses_list():
    numbers = list(range(1, 5))

    str = ['abcd', 'asdc', 'asdasda']

    list1 = ['xiaohou', 'xiaosun', 'xiaosong']

    list2 = ['1', '2', '3', '4', '5', '6', '7', '8']

    print("list1[0]:", list1[0])

    print("list2[1:5]:", list2[0:3])
    #
    # print(numbers)
    # print(len(numbers))
    # print(numbers[0])
    # print(numbers[1])

    # 首字母大写
    # print(str[0].title())


#     删除列表中重复的元素，并保持顺序不变
def delete_list(item):
    seen = set()
    for item in item:
        if item not in seen:
            yield item
            seen.add(item)


if __name__ == '__main__':
    a = ['3', '5', '10', '11', '0', '4', '25', '11', '0']
    print(list(delete_list(a)))
