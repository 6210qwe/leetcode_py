# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 786
标题: Search in a Sorted Array of Unknown Size
难度: medium
链接: https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/
题目类型: 数组、二分查找、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
702. 搜索长度未知的有序数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用指数搜索找到目标值的范围，然后在该范围内使用二分查找。

算法步骤:
1. 使用指数搜索确定目标值所在的范围。
2. 在确定的范围内使用二分查找找到目标值。

关键点:
- 指数搜索：通过逐步扩大步长来找到目标值的可能范围。
- 二分查找：在确定的范围内进行二分查找以找到目标值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Step 1: Exponential search to find the range
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1  # Double the right boundary

        # Step 2: Binary search within the found range
        while left <= right:
            mid = (left + right) // 2
            mid_value = reader.get(mid)
            
            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Target not found


Solution = create_solution(Solution)