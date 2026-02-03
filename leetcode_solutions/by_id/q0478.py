# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 478
标题: Generate Random Point in a Circle
难度: medium
链接: https://leetcode.cn/problems/generate-random-point-in-a-circle/
题目类型: 几何、数学、拒绝采样、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
478. 在圆内随机生成点 - 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 拒绝采样或极坐标方法

算法步骤:
1. 使用极坐标：随机角度和随机半径
2. 注意半径需要开方，保证均匀分布
3. 转换为直角坐标

关键点:
- 极坐标方法
- 半径需要开方保证均匀
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 常数时间
空间复杂度: O(1) - 只使用常数额外空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_random_point_in_a_circle(radius: float, x_center: float, y_center: float):
    """
    函数式接口 - 在圆内随机生成点
    
    实现思路:
    使用极坐标方法，随机角度和随机半径（需要开方）。
    
    Args:
        radius: 圆的半径
        x_center: 圆心x坐标
        y_center: 圆心y坐标
        
    Returns:
        随机点的坐标[x, y]
        
    Example:
        >>> point = generate_random_point_in_a_circle(1.0, 0.0, 0.0)
        >>> len(point) == 2
        True
    """
    import random
    import math
    
    # 随机角度
    theta = random.uniform(0, 2 * math.pi)
    # 随机半径（需要开方保证均匀分布）
    r = radius * math.sqrt(random.uniform(0, 1))
    
    x = x_center + r * math.cos(theta)
    y = y_center + r * math.sin(theta)
    
    return [x, y]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(generate_random_point_in_a_circle)
