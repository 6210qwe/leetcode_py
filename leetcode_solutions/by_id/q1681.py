# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1681
标题: Guess the Majority in a Hidden Array
难度: medium
链接: https://leetcode.cn/problems/guess-the-majority-in-a-hidden-array/
题目类型: 数组、数学、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1538. 找出隐藏数组中出现次数最多的元素 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过调用 `guessMajority` 函数来判断当前元素是否是多数元素，并记录每个元素的投票结果。最后根据投票结果确定多数元素。

算法步骤:
1. 初始化一个计数器 `count` 和一个变量 `majority` 来记录当前多数元素的索引。
2. 调用 `guessMajority` 函数，获取初始状态下的多数元素索引。
3. 遍历数组中的每个元素，调用 `guessMajority` 函数并更新计数器 `count` 和 `majority`。
4. 根据最终的计数器 `count` 确定多数元素的索引或返回 -1。

关键点:
- 通过调用 `guessMajority` 函数来判断当前元素是否是多数元素。
- 使用计数器来记录每个元素的投票结果。
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

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(guessMajority: 'GuessMajority') -> int:
    """
    函数式接口 - 实现
    """
    # 初始调用 guessMajority 获取初始状态下的多数元素索引
    majority = guessMajority(-1)
    count = 1  # 初始状态下多数元素的计数为1

    # 遍历数组中的每个元素
    for i in range(5):
        result = guessMajority(i)
        if result == majority:
            count += 1
        elif result != -1:
            count -= 1
            if count == 0:
                majority = result
                count = 1

    # 根据最终的计数器 count 确定多数元素的索引或返回 -1
    if count > 0:
        return majority
    else:
        return -1


Solution = create_solution(solution_function_name)