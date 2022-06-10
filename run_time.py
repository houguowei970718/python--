'''


Author: 小侯
Date: 2022-05-25 10:48:05
LastEditTime: 2022-06-08 09:04:59
LastEditors:    
Description: 
FilePath: \python算法\run_time.py
'''

"""
@Project : python算法 
@File : run_time.py
@Author : Administrator
@Data : 2022/5/25 10:48
"""

import time


def run_time(func):
    def test(*args, **kwargs):
        st_time = time.time()
        result = func(*args, **kwargs)

        sp_time = time.time()
        print("%s runing time: %s secs." % (func.__name__, sp_time - st_time))
        return result

    return test




a = (2+1)%12
print(a)