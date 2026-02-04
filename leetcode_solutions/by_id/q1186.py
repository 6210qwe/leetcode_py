# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1186
标题: Building H2O
难度: medium
链接: https://leetcode.cn/problems/building-h2o/
题目类型: 多线程
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1117. H2O 生成 - 现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。 存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。 氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。 这些线程应该三三成组突破屏障并能立即组合产生一个水分子。 你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。 换句话说: * 如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。 * 如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。 书写满足这些限制条件的氢、氧线程同步代码。 示例 1: 输入: water = "HOH" 输出: "HHO" 解释: "HOH" 和 "OHH" 依然都是有效解。 示例 2: 输入: water = "OOHHHH" 输出: "HHOHHO" 解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。 提示： * 3 * n == water.length * 1 <= n <= 20 * water[i] == 'O' or 'H' * 输入字符串 water 中的 'H' 总数将会是 2 * n 。 * 输入字符串 water 中的 'O' 总数将会是 n 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用锁和信号量来同步氢和氧线程。

算法步骤:
1. 初始化两个信号量 `hydrogen_semaphore` 和 `oxygen_semaphore`，分别用于控制氢和氧线程的数量。
2. 每当一个氢线程到达时，释放一个氢信号量，并等待氧信号量。
3. 每当一个氧线程到达时，释放一个氧信号量，并等待两个氢信号量。
4. 当氢和氧信号量都达到要求时，释放所有信号量，继续下一轮。

关键点:
- 使用信号量来控制线程的同步。
- 通过信号量的计数来确保每次生成一个水分子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每个线程的操作都是常数时间。
空间复杂度: O(1) - 只使用了固定的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from threading import Semaphore, Barrier
from typing import Callable

class H2O:
    def __init__(self):
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_semaphore.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydrogen_semaphore.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_semaphore.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oxygen_semaphore.release()

# 工厂函数
def create_solution():
    return H2O

Solution = create_solution