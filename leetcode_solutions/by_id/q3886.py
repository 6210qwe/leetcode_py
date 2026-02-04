# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3886
标题: Count Number of Trapezoids I
难度: medium
链接: https://leetcode.cn/problems/count-number-of-trapezoids-i/
题目类型: 几何、数组、哈希表、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3623. 统计梯形的数目 I - 给你一个二维整数数组 points，其中 points[i] = [xi, yi] 表示第 i 个点在笛卡尔平面上的坐标。 水平梯形 是一种凸四边形，具有 至少一对 水平边（即平行于 x 轴的边）。两条直线平行当且仅当它们的斜率相同。 返回可以从 points 中任意选择四个不同点组成的 水平梯形 数量。 由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。 示例 1： 输入： points = [[1,0],[2,0],[3,0],[2,2],[3,2]] 输出： 3 解释： [https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png] [https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png] [https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png] 有三种不同方式选择四个点组成一个水平梯形： * 使用点 [1,0]、[2,0]、[3,2] 和 [2,2]。 * 使用点 [2,0]、[3,0]、[3,2] 和 [2,2]。 * 使用点 [1,0]、[3,0]、[3,2] 和 [2,2]。 示例 2： 输入： points = [[0,0],[1,0],[0,1],[2,1]] 输出： 1 解释： [https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png] 只有一种方式可以组成一个水平梯形。 提示： * 4 <= points.length <= 105 * –108 <= xi, yi <= 108 * 所有点两两不同。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过哈希表记录每个 y 坐标上的点的数量，然后遍历所有可能的 y 坐标组合，计算每对 y 坐标之间的水平梯形数量。

算法步骤:
1. 使用哈希表记录每个 y 坐标上的点的数量。
2. 遍历所有可能的 y 坐标组合，计算每对 y 坐标之间的水平梯形数量。
3. 对于每对 y 坐标，使用组合公式计算水平梯形的数量，并累加到结果中。

关键点:
- 使用哈希表记录每个 y 坐标上的点的数量，以便快速查找和计算。
- 通过组合公式计算每对 y 坐标之间的水平梯形数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 points 的长度。需要遍历所有可能的 y 坐标组合。
空间复杂度: O(n)，用于存储每个 y 坐标上的点的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_number_of_trapezoids(points: List[List[int]]) -> int:
    """
    计算从 points 中任意选择四个不同点组成的水平梯形数量。
    """
    MOD = 10**9 + 7
    y_count = {}
    
    # 记录每个 y 坐标上的点的数量
    for x, y in points:
        if y not in y_count:
            y_count[y] = []
        y_count[y].append(x)
    
    result = 0
    
    # 遍历所有可能的 y 坐标组合
    for y1, xs1 in y_count.items():
        for y2, xs2 in y_count.items():
            if y1 >= y2:
                continue
            # 计算每对 y 坐标之间的水平梯形数量
            common_x = set(xs1) & set(xs2)
            if len(common_x) < 2:
                continue
            num_common_x = len(common_x)
            result += (num_common_x * (num_common_x - 1) // 2) * (len(xs1) - num_common_x) * (len(xs2) - num_common_x)
            result %= MOD
    
    return result

Solution = create_solution(count_number_of_trapezoids)