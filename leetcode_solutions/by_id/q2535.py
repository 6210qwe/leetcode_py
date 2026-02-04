# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2535
标题: Count Strictly Increasing Subarrays
难度: medium
链接: https://leetcode.cn/problems/count-strictly-increasing-subarrays/
题目类型: 数组、数学、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2393. 严格递增的子数组个数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算严格递增子数组的数量。

算法步骤:
1. 初始化一个变量 `count` 来记录严格递增子数组的数量。
2. 遍历数组，对于每个元素，检查它是否比前一个元素大。如果是，则更新当前子数组的长度，并将当前子数组的长度加到 `count` 中。
3. 如果当前元素不大于前一个元素，则重置当前子数组的长度为 1。

关键点:
- 使用一个变量 `current_length` 来记录当前严格递增子数组的长度。
- 每次遇到一个新的严格递增子数组时，将其长度加到 `count` 中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。我们只需要遍历数组一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_strictly_increasing_subarrays(nums: List[int]) -> int:
    """
    计算严格递增子数组的数量。
    """
    if not nums:
        return 0

    count = 0
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            count += current_length
        else:
            current_length = 1

    # 初始子数组的长度为 1 的情况
    count += len(nums)

    return count


Solution = create_solution(count_strictly_increasing_subarrays)