# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3449
标题: Maximum Hamming Distances
难度: hard
链接: https://leetcode.cn/problems/maximum-hamming-distances/
题目类型: 位运算、广度优先搜索、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3141. 最大汉明距离 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和动态规划来计算最大汉明距离。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示前 i 个元素中，第 j 位为 0 和 1 的数量差。
2. 遍历数组，更新 dp 数组。
3. 计算最大汉明距离。

关键点:
- 通过位运算统计每一位的 0 和 1 的数量差。
- 使用动态规划来优化计算过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max_num))，其中 n 是数组长度，max_num 是数组中的最大值。
空间复杂度: O(log(max_num))，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算最大汉明距离
    """
    if not nums:
        return 0

    max_num = max(nums)
    bit_length = max_num.bit_length()
    dp = [[0] * bit_length for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        num = nums[i - 1]
        for j in range(bit_length):
            if num & (1 << j):
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j] - 1

    max_hamming_distance = 0
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            hamming_distance = sum(abs(dp[j][k] - dp[i][k]) for k in range(bit_length))
            max_hamming_distance = max(max_hamming_distance, hamming_distance)

    return max_hamming_distance


Solution = create_solution(solution_function_name)