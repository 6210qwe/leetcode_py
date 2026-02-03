# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 469
标题: Convex Polygon
难度: medium
链接: https://leetcode.cn/problems/convex-polygon/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
469. 凸多边形 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算叉积，检查所有相邻边的转向是否一致

算法步骤:
1. 遍历所有相邻的三点，计算叉积
2. 如果所有叉积符号相同（都为正或都为负），则是凸多边形
3. 叉积符号不同则不是凸多边形

关键点:
- 使用叉积判断转向
- 注意处理共线情况
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历所有点一次
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def convex_polygon(points: List[List[int]]) -> bool:
    """
    函数式接口 - 凸多边形
    
    实现思路:
    计算所有相邻三点的叉积，检查转向是否一致。
    
    Args:
        points: 多边形顶点列表
        
    Returns:
        是否是凸多边形
        
    Example:
        >>> convex_polygon([[0,0],[1,0],[1,1],[0,1]])
        True
    """
    n = len(points)
    if n < 3:
        return False
    
    def cross_product(p1: List[int], p2: List[int], p3: List[int]) -> int:
        """计算叉积"""
        return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
    
    # 计算第一个叉积的符号
    first_sign = None
    
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]
        
        cross = cross_product(p1, p2, p3)
        
        if cross == 0:
            continue  # 共线，跳过
        
        if first_sign is None:
            first_sign = 1 if cross > 0 else -1
        else:
            current_sign = 1 if cross > 0 else -1
            if current_sign != first_sign:
                return False
    
    return True


# 自动生成Solution类（无需手动编写）
Solution = create_solution(convex_polygon)
