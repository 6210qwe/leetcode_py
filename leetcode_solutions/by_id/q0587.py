# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 587
标题: Erect the Fence
难度: hard
链接: https://leetcode.cn/problems/erect-the-fence/
题目类型: 几何、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
587. 安装栅栏 - 给定一个数组 trees，其中 trees[i] = [xi, yi] 表示树在花园中的位置。 你被要求用最短长度的绳子把整个花园围起来，因为绳子很贵。只有把 所有的树都围起来，花园才围得很好。 返回恰好位于围栏周边的树木的坐标。 示例 1: [https://assets.leetcode.com/uploads/2021/04/24/erect2-plane.jpg] 输入: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]] 输出: [[1,1],[2,0],[3,3],[2,4],[4,2]] 示例 2: [https://assets.leetcode.com/uploads/2021/04/24/erect1-plane.jpg] 输入: points = [[1,2],[2,2],[4,2]] 输出: [[4,2],[2,2],[1,2]] 注意: * 1 <= points.length <= 3000 * points[i].length == 2 * 0 <= xi, yi <= 100 * 所有给定的点都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Andrew's monotone chain 算法来找到凸包。

算法步骤:
1. 对所有点按 x 坐标升序排序，如果 x 坐标相同，则按 y 坐标升序排序。
2. 使用 Graham scan 算法构建下凸壳。
3. 使用 Graham scan 算法构建上凸壳。
4. 合并上下凸壳得到最终结果。

关键点:
- 使用叉积判断方向。
- 处理共线点时，选择 y 坐标最小的点。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是点的数量，主要由排序决定。
空间复杂度: O(n)，用于存储凸包的点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def solution_function_name(points: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 使用 Andrew's monotone chain 算法来找到凸包。
    """
    if len(points) < 3:
        return points

    # 按 x 坐标升序排序，如果 x 坐标相同，则按 y 坐标升序排序
    points.sort(key=lambda p: (p[0], p[1]))

    # 构建下凸壳
    lower_hull = []
    for point in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], point) < 0:
            lower_hull.pop()
        lower_hull.append(point)

    # 构建上凸壳
    upper_hull = []
    for point in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], point) < 0:
            upper_hull.pop()
        upper_hull.append(point)

    # 合并上下凸壳
    convex_hull = lower_hull[:-1] + upper_hull[:-1]
    return convex_hull


Solution = create_solution(solution_function_name)