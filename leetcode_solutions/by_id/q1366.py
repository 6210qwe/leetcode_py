# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1366
标题: First Unique Number
难度: medium
链接: https://leetcode.cn/problems/first-unique-number/
题目类型: 设计、队列、数组、哈希表、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1429. 第一个唯一数字 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个队列来维护当前数据流中的元素顺序，并使用一个哈希表来记录每个元素的出现次数。当需要获取第一个唯一数字时，从队列头部开始检查，直到找到第一个出现次数为1的元素。

算法步骤:
1. 初始化一个队列和一个哈希表。
2. 当有新元素加入数据流时，将其加入队列，并在哈希表中更新其出现次数。
3. 当需要获取第一个唯一数字时，从队列头部开始检查，直到找到第一个出现次数为1的元素。
4. 如果队列中没有出现次数为1的元素，则返回-1。

关键点:
- 使用队列来维护元素顺序。
- 使用哈希表来记录每个元素的出现次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 每次添加元素和获取第一个唯一数字的操作都是常数时间复杂度。
空间复杂度: O(n) - 最坏情况下，队列和哈希表都需要存储所有元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class FirstUniqueNumber:
    def __init__(self):
        self.queue = []
        self.counts = {}

    def add(self, value: int) -> None:
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1
            self.queue.append(value)

    def show_first_unique(self) -> int:
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.pop(0)
        if not self.queue:
            return -1
        return self.queue[0]


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(FirstUniqueNumber)