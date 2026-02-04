# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2658
标题: Count the Number of K-Big Indices
难度: hard
链接: https://leetcode.cn/problems/count-the-number-of-k-big-indices/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2519. 统计 K-Big 索引的数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈和二分查找来解决这个问题。

算法步骤:
1. 使用两个单调栈分别从左到右和从右到左遍历数组，记录每个位置左边和右边大于等于当前值的元素个数。
2. 对于每个位置，如果左边和右边的大于等于当前值的元素个数都大于等于 k，则该位置是 K-Big 索引。

关键点:
- 使用单调栈来记录左边和右边的大于等于当前值的元素个数。
- 使用二分查找来快速找到左边和右边的大于等于当前值的元素个数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_k_big_indices(nums: List[int], k: int) -> int:
    """
    函数式接口 - 统计 K-Big 索引的数量
    """
    n = len(nums)
    left_count = [0] * n
    right_count = [0] * n

    # 单调栈记录左边大于等于当前值的元素个数
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        if stack:
            left_count[i] = i - stack[-1] - 1
        stack.append(i)

    # 单调栈记录右边大于等于当前值的元素个数
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        if stack:
            right_count[i] = stack[-1] - i - 1
        stack.append(i)

    # 统计 K-Big 索引的数量
    count = 0
    for i in range(n):
        if left_count[i] >= k and right_count[i] >= k:
            count += 1

    return count


Solution = create_solution(count_k_big_indices)