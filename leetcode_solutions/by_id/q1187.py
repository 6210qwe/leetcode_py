# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1187
标题: Print FooBar Alternately
难度: medium
链接: https://leetcode.cn/problems/print-foobar-alternately/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1115. 交替打印 FooBar - 给你一个类： class FooBar { public void foo() { for (int i = 0; i < n; i++) { print("foo"); } } public void bar() { for (int i = 0; i < n; i++) { print("bar"); } } } 两个不同的线程将会共用一个 FooBar 实例： * 线程 A 将会调用 foo() 方法，而 * 线程 B 将会调用 bar() 方法 请设计修改程序，以确保 "foobar" 被输出 n 次。 示例 1： 输入：n = 1 输出："foobar" 解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。 示例 2： 输入：n = 2 输出："foobarfoobar" 解释："foobar" 将被输出两次。 提示： * 1 <= n <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用锁机制来控制两个线程的执行顺序。

算法步骤:
1. 初始化两个锁，一个用于控制 foo 的执行，另一个用于控制 bar 的执行。
2. 在 foo 方法中，先获取 foo 锁，打印 "foo"，然后释放 bar 锁。
3. 在 bar 方法中，先获取 bar 锁，打印 "bar"，然后释放 foo 锁。
4. 通过这种方式，确保 "foo" 和 "bar" 交替打印。

关键点:
- 使用锁机制来控制线程的执行顺序。
- 初始时，foo 锁处于解锁状态，bar 锁处于锁定状态，确保从 foo 开始。
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

from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()  # 初始时，bar 锁处于锁定状态

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()  # 获取 foo 锁
            printFoo()  # 打印 "foo"
            self.bar_lock.release()  # 释放 bar 锁

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()  # 获取 bar 锁
            printBar()  # 打印 "bar"
            self.foo_lock.release()  # 释放 foo 锁


# 示例调用
if __name__ == "__main__":
    from threading import Thread
    from typing import Callable

    def printFoo():
        print("foo", end="")

    def printBar():
        print("bar", end="")

    n = 2
    foobar = FooBar(n)

    t1 = Thread(target=foobar.foo, args=(printFoo,))
    t2 = Thread(target=foobar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()