# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1316
标题: Fizz Buzz Multithreaded
难度: medium
链接: https://leetcode.cn/problems/fizz-buzz-multithreaded/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1195. 交替打印字符串 - 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是： * 如果这个数字可以被 3 整除，输出 "fizz"。 * 如果这个数字可以被 5 整除，输出 "buzz"。 * 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。 例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。 假设有这么一个类： class FizzBuzz { public FizzBuzz(int n) { ... } // constructor public void fizz(printFizz) { ... } // only output "fizz" public void buzz(printBuzz) { ... } // only output "buzz" public void fizzbuzz(printFizzBuzz) { ... } // only output "fizzbuzz" public void number(printNumber) { ... } // only output the numbers } 请你实现一个有四个线程的多线程版 FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用： 1. 线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。 2. 线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。 3. 线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。 4. 线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。 提示： * 本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用锁和条件变量来控制多个线程的执行顺序。

算法步骤:
1. 初始化一个计数器 `current` 从 1 开始，并设置一个总长度 `n`。
2. 每个线程根据其特定条件（是否能被 3、5 或 3 和 5 整除）等待相应的条件变量。
3. 当满足条件时，相应的线程获取锁并打印结果，然后释放锁并将计数器加一。
4. 如果计数器达到 `n`，则所有线程结束。

关键点:
- 使用 `threading.Condition` 来控制线程的同步。
- 每个线程在满足条件时才打印并更新计数器。
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

import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    break
                if self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1
                    self.condition.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    break
                if self.current % 3 != 0 and self.current % 5 == 0:
                    printBuzz()
                    self.current += 1
                    self.condition.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    break
                if self.current % 3 == 0 and self.current % 5 == 0:
                    printFizzBuzz()
                    self.current += 1
                    self.condition.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    break
                if self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1
                    self.condition.notify_all()

# 示例用法
if __name__ == "__main__":
    import threading
    from typing import Callable

    def printFizz():
        print("fizz")

    def printBuzz():
        print("buzz")

    def printFizzBuzz():
        print("fizzbuzz")

    def printNumber(num: int):
        print(num)

    n = 15
    fizz_buzz = FizzBuzz(n)

    t1 = threading.Thread(target=fizz_buzz.fizz, args=(printFizz,))
    t2 = threading.Thread(target=fizz_buzz.buzz, args=(printBuzz,))
    t3 = threading.Thread(target=fizz_buzz.fizzbuzz, args=(printFizzBuzz,))
    t4 = threading.Thread(target=fizz_buzz.number, args=(printNumber,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()