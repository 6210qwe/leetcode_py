# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000292
标题: 数据流中的移动平均值
难度: easy
链接: https://leetcode.cn/problems/qIsx9U/
题目类型: 设计、队列、数组、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 041. 数据流中的移动平均值 - 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。 实现 MovingAverage 类： * MovingAverage(int size) 用窗口大小 size 初始化对象。 * double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。 示例： 输入： inputs = ["MovingAverage", "next", "next", "next", "next"] inputs = [[3], [1], [10], [3], [5]] 输出： [null, 1.0, 5.5, 4.66667, 6.0] 解释： MovingAverage movingAverage = new MovingAverage(3); movingAverage.next(1); // 返回 1.0 = 1 / 1 movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2 movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3 movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3 提示： * 1 <= size <= 1000 * -105 <= val <= 105 * 最多调用 next 方法 104 次 注意：本题与主站 346 题相同： https://leetcode.cn/problems/moving-average-from-data-stream/ [https://leetcode.cn/problems/moving-average-from-data-stream/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列来存储滑动窗口内的元素，并维护一个当前窗口内元素的总和。

算法步骤:
1. 初始化时，设置窗口大小，并初始化一个队列和当前窗口内元素的总和。
2. 每次调用 next 方法时，将新元素加入队列，并更新总和。
3. 如果队列的长度超过窗口大小，则移除队列的第一个元素，并从总和中减去该元素。
4. 计算并返回当前窗口内元素的平均值。

关键点:
- 使用队列来维护滑动窗口内的元素。
- 维护一个当前窗口内元素的总和，以避免每次重新计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次调用 next 方法的时间复杂度为 O(1)，因为只涉及队列的插入和删除操作。
空间复杂度: O(size) - 队列的最大长度为窗口大小 size。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.sum -= self.queue.pop(0)
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)


Solution = create_solution(MovingAverage)