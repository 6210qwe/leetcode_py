# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1216
标题: Print Zero Even Odd
难度: medium
链接: https://leetcode.cn/problems/print-zero-even-odd/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1116. 打印零与奇偶数 - 现有函数 printNumber 可以用一个整数参数调用，并输出该整数到控制台。 * 例如，调用 printNumber(7) 将会输出 7 到控制台。 给你类 ZeroEvenOdd 的一个实例，该类中有三个函数：zero、even 和 odd 。ZeroEvenOdd 的相同实例将会传递给三个不同线程： * 线程 A：调用 zero() ，只输出 0 * 线程 B：调用 even() ，只输出偶数 * 线程 C：调用 odd() ，只输出奇数 修改给出的类，以输出序列 "010203040506..." ，其中序列的长度必须为 2n 。 实现 ZeroEvenOdd 类： * ZeroEvenOdd(int n) 用数字 n 初始化对象，表示需要输出的数。 * void zero(printNumber) 调用 printNumber 以输出一个 0 。 * void even(printNumber) 调用printNumber 以输出偶数。 * void odd(printNumber) 调用 printNumber 以输出奇数。 示例 1： 输入：n = 2 输出："0102" 解释：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。 示例 2： 输入：n = 5 输出："0102030405" 提示： * 1 <= n <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个锁来控制 zero 和 even/odd 的交替输出。

算法步骤:
1. 初始化两个锁，一个用于 zero，一个用于 even/odd。
2. 在 zero 函数中，先输出 0，然后根据当前计数决定释放 even 或 odd 锁。
3. 在 even 和 odd 函数中，等待相应的锁，输出对应的数字，然后释放 zero 锁。

关键点:
- 使用锁来控制多线程的交替输出。
- 确保 zero 和 even/odd 之间的同步。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from threading import Lock, Barrier
from typing import Callable

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_odd_lock = Lock()
        self.even_odd_lock.acquire()
        self.barrier = Barrier(3)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.even_odd_lock.release()
            else:
                self.even_odd_lock.release()
            self.barrier.wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
            self.barrier.wait()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.even_odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
            self.barrier.wait()

def create_solution(solution_function_name):
    """
    工厂函数 - 创建并返回 Solution 类的实例
    """
    return solution_function_name

def solution_function_name(params):
    """
    函数式接口 - [待实现]
    """
    # 待实现: 实现最优解法
    pass

Solution = create_solution(solution_function_name)