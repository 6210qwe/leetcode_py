# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 149
标题: Max Points on a Line
难度: hard
链接: https://leetcode.cn/problems/max-points-on-a-line/
题目类型: 几何、数组、哈希表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
149. 直线上最多的点数 - 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。 示例 1： [https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg] 输入：points = [[1,1],[2,2],[3,3]] 输出：3 示例 2： [https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg] 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] 输出：4 提示： * 1 <= points.length <= 300 * points[i].length == 2 * -104 <= xi, yi <= 104 * points 中的所有点 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对于每个点，计算它与其他所有点的斜率，使用哈希表统计相同斜率的点数

算法步骤:
1. 对于每个点，计算它与其他所有点的斜率
2. 使用哈希表统计相同斜率的点数
3. 处理重复点和垂直线的特殊情况

关键点:
- 使用斜率作为键，处理特殊情况
- 时间复杂度O(n^2)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 需要遍历所有点对
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import defaultdict
from math import gcd
from leetcode_solutions.utils.solution import create_solution


def max_points_on_a_line(points: List[List[int]]) -> int:
    """
    函数式接口 - 直线上最多的点数
    
    实现思路:
    对于每个点，计算它与其他所有点的斜率，使用哈希表统计相同斜率的点数。
    
    Args:
        points: 点数组，每个点为[xi, yi]
        
    Returns:
        最多有多少个点在同一条直线上
        
    Example:
        >>> max_points_on_a_line([[1,1],[2,2],[3,3]])
        3
    """
    n = len(points)
    if n <= 2:
        return n
    
    max_points = 0
    
    for i in range(n):
        slope_count = defaultdict(int)
        same_point = 0
        current_max = 0
        
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            if x1 == x2 and y1 == y2:
                same_point += 1
            else:
                dx = x2 - x1
                dy = y2 - y1
                
                # 计算最大公约数，归一化斜率
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                slope = (dx, dy)
                slope_count[slope] += 1
                current_max = max(current_max, slope_count[slope])
        
        max_points = max(max_points, current_max + same_point + 1)
    
    return max_points


# 自动生成Solution类（无需手动编写）
Solution = create_solution(max_points_on_a_line)
