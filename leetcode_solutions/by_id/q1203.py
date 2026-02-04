# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1203
标题: Print in Order
难度: easy
链接: https://leetcode.cn/problems/print-in-order/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1114. 按序打印 - 给你一个类： public class Foo { public void first() { print("first"); } public void second() { print("second"); } public void third() { print("third"); } } 三个不同的线程 A、B、C 将会共用一个 Foo 实例。 * 线程 A 将会调用 first() 方法 * 线程 B 将会调用 second() 方法 * 线程 C 将会调用 third() 方法 请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。 提示： * 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。 * 你看到的输入格式主要是为了确保测试的全面性。 示例 1： 输入：nums = [1,2,3] 输出："firstsecondthird" 解释： 有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。正确的输出是 "firstsecondthird"。 示例 2： 输入：nums = [1,3,2] 输出："firstsecondthird" 解释： 输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正确的输出是 "firstsecondthird"。 提示： * nums 是 [1, 2, 3] 的一组排列
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用锁来确保按顺序执行

算法步骤:
1. 初始化两个锁，并将它们设置为锁定状态。
2. 在 `first` 方法中，打印 "first" 并释放第二个锁。
3. 在 `second` 方法中，等待第一个锁被释放，然后打印 "second" 并释放第三个锁。
4. 在 `third` 方法中，等待第二个锁被释放，然后打印 "third"。

关键点:
- 使用锁来控制线程的执行顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个方法的时间复杂度都是常数级别的。
空间复杂度: O(1) - 只使用了常数级别的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import threading

class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock2:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

# 示例调用
def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")

foo = Foo()
from threading import Thread

t1 = Thread(target=foo.first, args=(printFirst,))
t2 = Thread(target=foo.second, args=(printSecond,))
t3 = Thread(target=foo.third, args=(printThird,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()