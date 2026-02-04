# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100337
标题: 设计自助结算系统
难度: medium
链接: https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/
题目类型: 设计、队列、单调队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 184. 设计自助结算系统 - 请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有： * get_max()：获取结算商品中的最高价格，如果队列为空，则返回 -1 * add(value)：将价格为 value 的商品加入待结算商品队列的尾部 * remove()：移除第一个待结算的商品价格，如果队列为空，则返回 -1 注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1) 示例 1： 输入: ["Checkout","add","add","get_max","remove","get_max"] [[],[4],[7],[],[],[]] 输出: [null,null,null,7,4,7] 示例 2： 输入: ["Checkout","remove","get_max"] [[],[],[]] 输出: [null,-1,-1] 提示： * 1 <= get_max, add, remove 的总操作数 <= 10000 * 1 <= value <= 10^5
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个队列，一个普通队列 `queue` 用于存储所有商品的价格，另一个双端队列 `max_queue` 用于维护当前队列中的最大值。

算法步骤:
1. 初始化两个队列 `queue` 和 `max_queue`。
2. `add(value)` 操作时，将 `value` 加入 `queue`，同时在 `max_queue` 中维护当前的最大值。
3. `remove()` 操作时，从 `queue` 中移除第一个元素，如果该元素是当前最大值，则也从 `max_queue` 中移除。
4. `get_max()` 操作时，直接返回 `max_queue` 的第一个元素。

关键点:
- `max_queue` 维护的是当前队列中的最大值，且保持单调递减。
- 在 `add` 操作时，确保 `max_queue` 的单调性。
- 在 `remove` 操作时，检查并移除 `max_queue` 中的过期最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) 均摊时间复杂度
空间复杂度: O(n) 其中 n 是队列中元素的数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Checkout:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def get_max(self) -> int:
        if not self.max_queue:
            return -1
        return self.max_queue[0]

    def add(self, value: int) -> None:
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def remove(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.pop(0)
        if value == self.max_queue[0]:
            self.max_queue.pop(0)
        return value


Solution = create_solution(Checkout)