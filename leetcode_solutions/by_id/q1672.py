# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1672
标题: Find the Index of the Large Integer
难度: medium
链接: https://leetcode.cn/problems/find-the-index-of-the-large-integer/
题目类型: 数组、二分查找、交互
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1533. 找到最大整数的索引 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到数组中最大的整数的索引。

算法步骤:
1. 初始化左右指针 left 和 right 分别为 0 和 n-1。
2. 进行二分查找：
   - 计算中间位置 mid。
   - 比较 nums[mid] 和 nums[mid+1] 的大小。
   - 如果 nums[mid] < nums[mid+1]，说明最大值在右半部分，更新 left = mid + 1。
   - 否则，最大值在左半部分或就是 mid，更新 right = mid。
3. 最终 left 指向的就是最大值的索引。

关键点:
- 通过比较相邻元素的大小来确定最大值的位置。
- 二分查找的时间复杂度为 O(log n)。
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


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 使用二分查找找到数组中最大整数的索引
    """
    n = len(nums)
    left, right = 0, n - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left


Solution = create_solution(solution_function_name)