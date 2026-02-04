# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2074
标题: Erect the Fence II
难度: hard
链接: https://leetcode.cn/problems/erect-the-fence-ii/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1924. 安装栅栏 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用凸包算法（Graham Scan）来找到所有点的最小凸包，然后计算每个点到凸包的距离。

算法步骤:
1. 找到最左下角的点作为起始点。
2. 根据极角对其他点进行排序。
3. 使用 Graham Scan 算法构建凸包。
4. 计算每个点到凸包的距离，并返回结果。

关键点:
- 使用叉积来判断点的位置关系。
- 使用栈来维护凸包的顶点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是点的数量。排序操作的时间复杂度是 O(n log n)，Graham Scan 的时间复杂度是 O(n)。
空间复杂度: O(n)，用于存储排序后的点和凸包的顶点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
import math

def cross_product(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """计算向量 o->a 和 o->b 的叉积"""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """计算两点之间的欧几里得距离"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def graham_scan(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """使用 Graham Scan 算法构建凸包"""
    if len(points) < 3:
        return points

    # 找到最左下角的点
    start = min(points)
    points.remove(start)

    # 按极角排序
    points.sort(key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), distance(start, p)))

    # 构建凸包
    hull = [start]
    for point in points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    return hull

def solution_function_name(trees: List[List[int]], target: List[int]) -> List[float]:
    """
    函数式接口 - 计算每个树到凸包的距离
    """
    # 将目标点添加到树木列表中
    trees.append(target)
    
    # 构建凸包
    hull = graham_scan(trees)
    
    # 计算每个点到凸包的距离
    distances = []
    for tree in trees:
        min_distance = float('inf')
        for i in range(len(hull)):
            j = (i + 1) % len(hull)
            # 计算点到线段的距离
            d = abs(cross_product(hull[i], hull[j], tree)) / distance(hull[i], hull[j])
            min_distance = min(min_distance, d)
        distances.append(min_distance)
    
    # 移除目标点对应的距离
    distances.pop()
    
    return distances

Solution = create_solution(solution_function_name)