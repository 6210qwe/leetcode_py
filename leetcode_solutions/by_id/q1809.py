# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1809
标题: Sum Of Special Evenly-Spaced Elements In Array
难度: hard
链接: https://leetcode.cn/problems/sum-of-special-evenly-spaced-elements-in-array/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1714. 数组中特殊等间距元素的和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算数组中特殊等间距元素的和。

算法步骤:
1. 初始化一个动态规划表 dp，其中 dp[i][j] 表示以第 i 个元素为起点，间隔为 j 的子序列的和。
2. 遍历数组，对于每个元素 nums[i]，更新 dp 表。
3. 最终结果是 dp 表中的最大值。

关键点:
- 动态规划表 dp 的初始化和更新。
- 通过遍历数组来更新 dp 表。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sum_of_special_evenly_spaced_elements(nums: List[int]) -> int:
    """
    计算数组中特殊等间距元素的和
    """
    n = len(nums)
    if n == 0:
        return 0

    # 初始化 dp 表
    dp = [[0] * n for _ in range(n)]

    # 更新 dp 表
    for i in range(n):
        for j in range(1, (n - i) // 2 + 1):
            if i + 2 * j < n:
                dp[i][j] = nums[i] + dp[i + j][j]

    # 找到 dp 表中的最大值
    max_sum = 0
    for i in range(n):
        for j in range(1, (n - i) // 2 + 1):
            max_sum = max(max_sum, dp[i][j])

    return max_sum


Solution = create_solution(sum_of_special_evenly_spaced_elements)