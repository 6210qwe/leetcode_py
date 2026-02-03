# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 259
标题: 3Sum Smaller
难度: medium
链接: https://leetcode.cn/problems/3sum-smaller/
题目类型: 数组、双指针、二分查找、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
259. 较小的三数之和 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 双指针，固定第一个数，用双指针找后两个数

算法步骤:
1. 排序数组
2. 固定第一个数，使用双指针找后两个数
3. 如果三数之和<target，则left到right-1的所有组合都满足

关键点:
- 双指针优化
- 时间复杂度O(n^2)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 排序O(n log n) + 双指针O(n^2)
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def three_sum_smaller(nums: List[int], target: int) -> int:
    """
    函数式接口 - 较小的三数之和
    
    实现思路:
    双指针：固定第一个数，用双指针找后两个数。
    
    Args:
        nums: 整数数组
        target: 目标值
        
    Returns:
        满足条件的三元组数量
        
    Example:
        >>> three_sum_smaller([-2,0,1,3], 2)
        2
    """
    nums.sort()
    count = 0
    n = len(nums)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < target:
                # 所有left到right-1的组合都满足
                count += right - left
                left += 1
            else:
                right -= 1
    
    return count


# 自动生成Solution类（无需手动编写）
Solution = create_solution(three_sum_smaller)
