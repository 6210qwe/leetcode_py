# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 519
标题: Widest Pair of Indices With Equal Range Sum
难度: medium
链接: https://leetcode.cn/problems/widest-pair-of-indices-with-equal-range-sum/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1983. 范围和相等的最宽索引对 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来记录每个前缀和第一次出现的位置，从而找到最宽的索引对。

算法步骤:
1. 计算数组的前缀和。
2. 使用哈希表记录每个前缀和第一次出现的位置。
3. 遍历前缀和数组，对于每个前缀和，检查其在哈希表中是否存在，如果存在，则计算当前索引与哈希表中记录的索引之间的距离，并更新最大宽度。

关键点:
- 使用哈希表记录前缀和第一次出现的位置，确保找到的索引对是最宽的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
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
    函数式接口 - 实现最优解法
    """
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    max_width = 0
    first_occurrence = {}
    for i, sum_ in enumerate(prefix_sum):
        if sum_ in first_occurrence:
            max_width = max(max_width, i - first_occurrence[sum_])
        else:
            first_occurrence[sum_] = i

    return max_width


Solution = create_solution(solution_function_name)