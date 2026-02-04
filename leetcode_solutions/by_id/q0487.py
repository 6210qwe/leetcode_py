# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 487
标题: Max Consecutive Ones II
难度: medium
链接: https://leetcode.cn/problems/max-consecutive-ones-ii/
题目类型: 数组、动态规划、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
487. 最大连续1的个数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到最大连续1的个数，允许翻转一个0为1

算法步骤:
1. 初始化两个指针 left 和 right，分别表示滑动窗口的左右边界
2. 初始化变量 max_ones 用于记录最大连续1的个数
3. 初始化变量 zero_count 用于记录当前窗口内0的数量
4. 移动右指针 right，扩展窗口
5. 如果 zero_count 超过1，则移动左指针 left，缩小窗口
6. 更新 max_ones
7. 返回 max_ones

关键点:
- 使用滑动窗口来保持窗口内的0的数量不超过1
- 通过移动左右指针来维护窗口的大小
- 时间复杂度和空间复杂度优化
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只遍历数组一次
空间复杂度: O(1) - 只使用常数级额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_consecutive_ones_ii(nums: List[int]) -> int:
    """
    函数式接口 - 找到数组中最大连续1的个数，允许翻转一个0为1
    
    实现思路:
    使用滑动窗口来找到最大连续1的个数，允许翻转一个0为1
    
    Args:
        nums: 输入的二进制数组
        
    Returns:
        最大连续1的个数
        
    Example:
        >>> max_consecutive_ones_ii([1,0,1,1,0])
        4
    """
    left = 0
    zero_count = 0
    max_ones = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_ones = max(max_ones, right - left + 1)
    
    return max_ones


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_consecutive_ones_ii)