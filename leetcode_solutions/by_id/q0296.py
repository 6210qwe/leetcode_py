# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 296
标题: Best Meeting Point
难度: hard
链接: https://leetcode.cn/problems/best-meeting-point/
题目类型: 数组、数学、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
296. 最佳的碰头地点 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 中位数是最优解，分别计算行和列的中位数

算法步骤:
1. 收集所有1的行坐标和列坐标
2. 分别排序
3. 中位数位置就是最佳碰头点
4. 计算所有点到中位数的距离和

关键点:
- 中位数最优
- 时间复杂度O(m*n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - 遍历矩阵
空间复杂度: O(k) - k为1的个数
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_total_distance(grid: List[List[int]]) -> int:
    """
    函数式接口 - 最佳的碰头地点
    
    实现思路:
    中位数是最优解：分别计算行和列的中位数。
    
    Args:
        grid: 网格矩阵（1表示人）
        
    Returns:
        最小总距离
        
    Example:
        >>> min_total_distance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
        6
    """
    rows, cols = [], []
    m, n = len(grid), len(grid[0])
    
    # 收集所有1的坐标
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)
    
    # 排序
    rows.sort()
    cols.sort()
    
    # 中位数位置
    mid_row = rows[len(rows) // 2]
    mid_col = cols[len(cols) // 2]
    
    # 计算总距离
    distance = 0
    for r in rows:
        distance += abs(r - mid_row)
    for c in cols:
        distance += abs(c - mid_col)
    
    return distance


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_total_distance)
