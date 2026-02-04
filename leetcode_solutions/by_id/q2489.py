# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2489
标题: Sort Array by Moving Items to Empty Space
难度: hard
链接: https://leetcode.cn/problems/sort-array-by-moving-items-to-empty-space/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2459. 通过移动项目到空白区域来排序数组 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过找到空位并移动元素来排序数组。

算法步骤:
1. 找到数组中的空位（值为0的位置）。
2. 从左到右遍历数组，将每个元素移动到其正确的位置，利用空位进行交换。
3. 如果当前元素已经在正确位置，则跳过。
4. 如果当前元素不在正确位置且空位在当前元素之后，则交换当前元素和空位的值。
5. 重复上述步骤直到数组有序。

关键点:
- 利用空位进行交换，避免额外的空间开销。
- 通过贪心策略确保每次移动都是最优的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 在最坏情况下，每个元素都需要多次移动。
空间复杂度: O(1) - 只使用常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def sortArrayByMovingItems(nums: List[int]) -> int:
    """
    函数式接口 - 通过移动项目到空白区域来排序数组
    """
    n = len(nums)
    moves = 0
    i = 0
    
    while i < n:
        if nums[i] == 0 or nums[i] == i + 1:
            i += 1
            continue
        
        correct_pos = nums[i] - 1
        if nums[correct_pos] == 0:
            nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            moves += 1
        else:
            nums[correct_pos], nums[i] = nums[i], 0
            moves += 1
            i -= 1  # Recheck the current position
        i += 1
    
    return moves


Solution = create_solution(sortArrayByMovingItems)