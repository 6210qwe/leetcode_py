# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 265
标题: Paint House II
难度: hard
链接: https://leetcode.cn/problems/paint-house-ii/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
265. 粉刷房子 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，记录最小值和次小值

算法步骤:
1. dp[i][j]表示第i个房子涂第j种颜色的最小成本
2. 记录上一行的最小值和次小值及其颜色
3. 当前行选择颜色时，如果颜色与最小值颜色相同，使用次小值

关键点:
- 记录最小值和次小值优化
- 时间复杂度O(n*k)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*k) - n为房子数，k为颜色数
空间复杂度: O(k) - 优化后空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_cost_ii(costs: List[List[int]]) -> int:
    """
    函数式接口 - 粉刷房子 II
    
    实现思路:
    动态规划：记录最小值和次小值优化。
    
    Args:
        costs: 每个房子涂k种颜色的成本
        
    Returns:
        最小成本
        
    Example:
        >>> min_cost_ii([[1,5,3],[2,9,4]])
        5
    """
    if not costs:
        return 0
    
    n, k = len(costs), len(costs[0])
    
    # 记录上一行的最小值和次小值
    min1, min2 = 0, 0
    idx1 = -1
    
    for i in range(n):
        # 当前行的最小值和次小值
        cur_min1, cur_min2 = float('inf'), float('inf')
        cur_idx1 = -1
        
        for j in range(k):
            # 计算当前颜色成本
            cost = costs[i][j] + (min2 if j == idx1 else min1)
            
            if cost < cur_min1:
                cur_min2 = cur_min1
                cur_min1 = cost
                cur_idx1 = j
            elif cost < cur_min2:
                cur_min2 = cost
        
        min1, min2 = cur_min1, cur_min2
        idx1 = cur_idx1
    
    return min1


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_cost_ii)
